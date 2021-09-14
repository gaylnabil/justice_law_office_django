# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Cybrosys Technologies(<http://www.cybrosys.com>).
#    Author: cybrosys(<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################
from datetime import datetime
import time
import binascii
from .zk_nga import Command
from struct import pack, unpack
from .zkconst import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math
from models import dbconnection
from threading import Thread
import keyboard
import dotenv
import os
import logging

logger = logging.getLogger(__name__)


dotenv.load_dotenv(dotenv.find_dotenv(), override=True)


def getSizeAttendance(self):
    """Checks a returned packet to see if it returned CMD_PREPARE_DATA,
    indicating that data packets are to be sent

    Returns the amount of bytes that are going to be sent"""
    command = unpack('HHHH', self.data_recv[:8])[0]
    if command == CMD_PREPARE_DATA:
        size = unpack('I', self.data_recv[8:12])[0]
        return size
    else:
        return False


def bytes_to_num(byte_array):
    num = 0

    for _, byte in enumerate(byte_array):
        num = (num * 256) + byte

    return num


def byte_array_to_time(byte_array):
    seconds_since_2000 = bytes_to_num(byte_array)
    # print('seconds_since_2000 : ', seconds_since_2000)

    sec = seconds_since_2000 % 60
    # print('second : ', sec)

    seconds_since_2000 = math.floor(seconds_since_2000 / 60)
    minute = seconds_since_2000 % 60
    # print('minute : ', minute)

    seconds_since_2000 = math.floor(seconds_since_2000 / 60)
    hour = seconds_since_2000 % 24
    # print('hour : ', hour)

    seconds_since_2000 = math.floor(seconds_since_2000 / 24)
    day = (seconds_since_2000 % 31) + 1
    # print('day : ', day)

    seconds_since_2000 = math.floor(seconds_since_2000 / 31)
    month = (seconds_since_2000 % 12) + 1
    # print('month : ', month)

    seconds_since_2000 = math.floor(seconds_since_2000 / 12)
    year = seconds_since_2000 + 2000
    # print('year : ', year)

    date_time_str = f'{year}-{month}-{day} {hour}:{minute}:{sec}'

    return datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')


def set_user_last_event(con, record):
    query = """ UPDATE users
                SET last_event_id=%s, status=%s
                WHERE pin = %s;"""

    con.execute_query(query, record)
    con.commit()


def flag_attendance(con, data):
    # query ="""SELECT u.pin as user_pin, u.status, a.id, a.pin as attendance_pin, a.status as attendance_status
    # FROM users u, attendance a
    # where u.pin = a.pin and u.status = a.status  and a.id = u.last_event_id and a.status=N'in' order by a.id desc limit 1; """
    query = """UPDATE attendance
            SET flag = true 
            WHERE pin = %s and 
			status = %s and 
			id = (select max(id) from attendance where pin = %s);"""

    con.execute_query(query, data)
    print("flag_attendance :", data)
    con.commit()


def status_from_byte_array(line):

    alarm_status = [line[0], line[1], line[2], line[3]]
    dss_status = [line[4], line[5], line[6], line[7]]
    verified = line[8]
    event_type = line[10]
    status = line[11]  # in or out
    time_second = byte_array_to_time([line[15], line[14], line[13],
                                      line[12]])

    return (str(0), str(0), str(verified), '0',
            str(event_type), str(status), time_second.strftime("%Y-%m-%d %H:%M:%S"))


def event_from_byte_array(line):
    card_no = bytes_to_num([line[3], line[2], line[1],
                            line[0]])

    pin = bytes_to_num([line[7], line[6], line[5],
                        line[4]])

    verified = line[8]
    door_id = line[9]

    event_type = line[10]
    status = 'in' if line[11] == 1 else 'out'  # in or out

    time_second = byte_array_to_time([line[15], line[14], line[13],
                                      line[12]])

    return (str(card_no), str(pin), str(verified), str(door_id),
            str(event_type), status, time_second.strftime("%Y-%m-%d %H:%M:%S"))


def reverseHex(hexstr):
    tmp = ''
    for i in reversed(range(int(len(hexstr)/2))):
        tmp += hexstr[i*2:(i*2)+2]

    return tmp


def zkgetattendance(self):
    """Start a connection with the time clock"""
    try:
        con = dbconnection.DbConnection(
            os.environ.get('USER', str),
            os.environ.get('PASSWORD', str),
            os.environ.get('HOST', str),
            os.environ.get('PORT', int),
            os.environ.get('DATABASE_NAME', str)
        )

        # print('USER : ', os.environ.get('USER', str))
        # print('PASSWORD : ', os.environ.get('PASSWORD', str))
        # print('HOST : ', os.environ.get('HOST', str))
        # print('PORT : ', os.environ.get('PORT', int))
        # print('DATABASE_NAME : ', os.environ.get('DATABASE_NAME', str))

        index = 0

        query = """INSERT INTO attendance
                    (card_no, pin, verified, door_id, event_type, status, date_event)
                    VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id """

        buf = self.nga.create_buffer(Command.C3_COMMAND_RTLOG)

        while True:

            self.zkclient.send(buf)
            self.data_recv = self.zkclient.recv(1024)
            index += 1
            self.nga.request_number += 1

            received_data = self.data_recv[5:-3]

            if len(received_data) == 16:

                record = status_from_byte_array(received_data)
                print("buffer : ", buf)
                print("record : ", record)
                # logger.info("record : ", record)

                if received_data[10] != 255:  # bagde checked
                    record = event_from_byte_array(received_data)

                    flag_attendance(con, (record[1], record[5], record[1]))

                    last_id = con.execute_query(query, record)

                    print("last_id : ", last_id)

                    set_user_last_event(con, (last_id, record[5], record[1]))

                # print("Data => self.data_recv : ", index, received_data)
                # print("Data => self.data_recv Full : ", index, self.data_recv)

                time.sleep(2)

            if keyboard.is_pressed('q' or 'Q'):
                break

        con.close()
        # self.nga.request_number += 1
        # self.session_id = [self.data_recv[6],  self.data_recv[5]]
        # self.nga.nga_session_id = self.session_id
        print("Version => self.data_recv : ", self.data_recv)
        print("Version => self.data_recv .hex(): ", self.data_recv.hex())
        print("self.session_id  : ", self.session_id)

        return self.data_recv
    except:
        return False


def zkgetattendance_with_form(self):
    """Start a connection with the time clock"""

    con = dbconnection.DbConnection(
        'postgres', 'gonvspito2011', '127.0.0.1', 5432, 'zkteco')
    index = 0
    data_bytes = bytes()
    query = """INSERT INTO attendance
                (card_no, pin, verified, door_id, event_type, status, date_event)
                VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id """

    buf = self.nga.create_buffer(Command.C3_COMMAND_RTLOG)
    while self.start:

        self.zkclient.send(buf)
        self.data_recv = self.zkclient.recv(1032)
        index += 1
        self.nga.request_number += 1

        received_data = self.data_recv[5:-3]

        if len(received_data) == 16:

            print("received_data : ", received_data)
            record = status_from_byte_array(received_data)

            if received_data[10] != 255:  # bagde checked
                record = event_from_byte_array(received_data)

                flag_attendance(con, (record[1], record[5], record[1]))

                last_id = con.execute_query(query, record)

                print("last_id : ", last_id)

                set_user_last_event(con, (last_id, record[5], record[1]))

            # values = (1, "pin10", "ver", "d1", 'evnt01', 'stat11', datetime.now())

            self.iid += 1
            self.tree_att.insert(parent='', index='end',
                                 iid=self.iid, text="", values=record)
            self.tree_att.yview_moveto(1)

            # data_bytes += self.data_recv
            print("Data => self.data_recv : ", index, self.data_recv[5:-3])
            print("Data => self.data_recv Full : ", index, self.data_recv)
            print("Data => self.data_recv : hex : ",
                  self.data_recv[5:-3].hex())
            print("Version => self.data_recv Length : ",
                  len(self.data_recv[5:-3]))

            time.sleep(2)

    con.close()
    print('data_bytes : ', data_bytes)
    print('data_decode : ', data_bytes.decode('utf-8', errors='ignore'))

    print("Version => self.data_recv : ", self.data_recv)
    print("Version => self.data_recv : ", self.data_recv[16:-1])

    # self.nga.request_number += 1

    # self.session_id = [self.data_recv[6],  self.data_recv[5]]
    # self.nga.nga_session_id = self.session_id

    print("Version => self.data_recv .hex(): ", self.data_recv.hex())
    print("self.session_id  : ", self.session_id)

    # print("Data : ", data)
    # data = bytes(data)
    # print("Version =>  self.data_recv[1:3] : ",  self.data_recv[3:4].hex())
    try:
        # self.data_recv, addr = self.zkclient.recvfrom(1024)
        # self.session_id = unpack('HHHH', self.data_recv[:8])[2]
        return self.data_recv[8:]
    except:
        return False


def start_click(self):

    self.start = True
    # messagebox.showinfo(title="Start Click",
    #                     message=f"Good job you did it ! {self.start }")
    self.my_thread = Thread(target=zkgetattendance, args=(self,))
    self.my_thread.start()


def stop_click(self):
    self.start = False
    # messagebox.showinfo(title="Stop Click",
    #                     message=f"Stop it => {self.start }")

    # self.my_thread.stop()


def form_show(self):
    self.iid = 0
    root = Tk(className='ZKteco - C3-100 FingerPrint')
    root.geometry('600x400')

    columns = ("card_no", "pin", "verified", "door_id",
               "event_type", "status", "date_event")

    self.tree_att = ttk.Treeview(root, selectmode="extended", columns=columns)

    self.tree_att.column('#0', width=0, minwidth=0, stretch=NO)
    self.tree_att.column('card_no', anchor=CENTER, width=20, stretch=YES)
    self.tree_att.column('pin', anchor=W, width=20, stretch=YES)
    self.tree_att.column('verified',  anchor=W, width=60, stretch=YES)
    self.tree_att.column('door_id',  anchor=W, width=60, stretch=YES)
    self.tree_att.column('event_type',  anchor=W, width=60, stretch=YES)
    self.tree_att.column('status',  anchor=W, width=40, stretch=YES)
    self.tree_att.column('date_event',  anchor=W, width=120, stretch=YES)

    self.tree_att.heading('#0', text='', anchor=W)
    self.tree_att.heading('card_no', text='ID', anchor=CENTER)
    self.tree_att.heading('pin', text='Pin', anchor=W)
    self.tree_att.heading('verified', text='Verified', anchor=W)
    self.tree_att.heading('door_id', text='Door ID', anchor=W)
    self.tree_att.heading('event_type', text='Event Type', anchor=W)
    self.tree_att.heading('status', text='Status', anchor=W)
    self.tree_att.heading('date_event', text='Date Event', anchor=W)

    # Add Data
    # values = (1, "pin10", "ver", "d1", 'evnt01', 'stat11', datetime.now())
    # self.tree_att.insert(parent='', index='end', iid=0, text="", values=values)

    # tree_att.pack(pady=10, padx=10)
    self.tree_att.grid(column=0, row=2, columnspan=2, sticky='nsew', padx=20)

    vsb = ttk.Scrollbar(root, orient="vertical", command=self.tree_att.yview)
    vsb.place(relx=0.672, rely=0.05, relheight=0.60, relwidth=0.020)
    # vsb.pack(side=RIGHT, fill=Y)
    self.tree_att.configure(yscrollcommand=vsb.set)

    button_start = Button(root, text="Start",
                          command=lambda: start_click(self))

    button_stop = Button(root, text="Stop", command=lambda: stop_click(self))
    button_start.grid(column=0, row=0, sticky=N)
    button_stop.grid(column=1, row=0,  sticky=N)
    root.mainloop()


def zkgetattendance1(self):
    """Start a connection with the time clock"""
    command = CMD_ATTLOG_RRQ
    command_string = ''
    chksum = 0
    session_id = self.session_id
    reply_id = unpack('HHHH', self.data_recv[:8])[3]

    buf = self.createHeader(command, chksum, session_id,
                            reply_id, command_string)

    self.zkclient.sendto(buf, self.address)
    # print buf.encode("hex")
    try:
        self.data_recv, addr = self.zkclient.recvfrom(1024)

        if getSizeAttendance(self):

            bytes = getSizeAttendance(self)

            while bytes > 0:
                data_recv, addr = self.zkclient.recvfrom(1032)
                self.attendancedata.append(data_recv)
                bytes -= 1024

            self.session_id = unpack('HHHH', self.data_recv[:8])[2]
            data_recv = self.zkclient.recvfrom(8)

        attendance = []
        if len(self.attendancedata) > 0:
            # The first 4 bytes don't seem to be related to the user
            for x in range(len(self.attendancedata)):
                if x > 0:
                    self.attendancedata[x] = self.attendancedata[x][8:]

            attendancedata = b''.join(self.attendancedata)

            attendancedata = attendancedata[14:]

            # while len(attendancedata) > 40:
            while len(attendancedata):

                uid, state, timestamp, space = unpack(
                    '24s1s4s11s', attendancedata.ljust(40)[:40])

                # Clean up some messy characters from the user name
                # uid = unicode(uid.strip('\x00|\x01\x10x'), errors='ignore')
                uid = uid.split(b'\x00', 1)[0].decode('utf-8')
                # print "%s, %s, %s" % (uid, state, decode_time( int( reverseHex( timestamp.encode('hex') ), 16 ) ) )

                attendance.append((uid, int(binascii.hexlify(state), 16), decode_time(
                    int(reverseHex(binascii.hexlify(timestamp).decode('utf-8')), 16))))

                attendancedata = attendancedata[40:]

        return attendance
    except:
        raise
        return False


def zkclearattendance(self):
    """Start a connection with the time clock"""
    command = CMD_CLEAR_ATTLOG
    command_string = ''
    chksum = 0
    session_id = self.session_id
    reply_id = unpack('HHHH', self.data_recv[:8])[3]

    buf = self.createHeader(command, chksum, session_id,
                            reply_id, command_string)
    self.zkclient.sendto(buf, self.address)
    # print buf.encode("hex")
    try:
        self.data_recv, addr = self.zkclient.recvfrom(1024)
        self.session_id = unpack('HHHH', self.data_recv[:8])[2]
        return self.data_recv[8:]
    except:
        return False
