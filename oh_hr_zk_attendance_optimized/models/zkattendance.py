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

    con.execute_query(query, data)
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

    print('USERNAME ENV : ',   os.environ.get('USERNAME', str))
    print('PASSWORD : ', os.environ.get('PASSWORD', str))
    print('HOST : ', os.environ.get('HOST', str))
    print('PORT : ', os.environ.get('PORT', int))
    print('DATABASE_NAME : ', os.environ.get('DATABASE_NAME', str))

    con = dbconnection.DbConnection(
        os.environ.get('USERNAME', str),
        os.environ.get('PASSWORD', str),
        os.environ.get('HOST', str),
        os.environ.get('PORT', int),
        os.environ.get('DATABASE_NAME', str)
    )

    try:

        index = 0

        query = """INSERT INTO attendance
                    (card_no, pin, verified, door_id,
                     event_type, status, date_event)
                    VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id """

        buf = self.nga.create_buffer(Command.C3_COMMAND_RTLOG)
        while True:

            self.zkclient.send(buf)
            self.data_recv = self.zkclient.recv(1032)
            index += 1
            self.nga.request_number += 1

            received_data = self.data_recv[5:-3]

            if len(received_data) == 16:

                record = status_from_byte_array(received_data)

                print("record  : ", record)

                if received_data[10] != 255:  # bagde checked
                    record = event_from_byte_array(received_data)

                    flag_attendance(con, (record[1], record[5], record[1]))

                    last_id = con.execute_query(query, record)

                    set_user_last_event(con, (last_id, record[5], record[1]))

                time.sleep(2)

            # if keyboard.is_pressed('q' or 'Q'):
            #     break

    except:
        self.data_recv = False

    con.close()
    print("self.session_id  : ", self.session_id)

    return self.data_recv


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
