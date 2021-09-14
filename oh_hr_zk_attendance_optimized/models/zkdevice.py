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
from models.zk_nga import Command
from struct import pack, unpack
from .zkconst import *


def zkdevicedata(self, parameters=None):
    """ Get Device Data """

    buf = self.nga.create_buffer(Command.C3_COMMAND_GETDEVICEDATA, parameters)

    # buf = b'\xaa\x01\x08\x07\x00\x02\x03\x01\x02\x03\x00\x00\x4c\xad\x55'  # userauthorize
    #     0   1  2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17

    # buf = b'\xaa\x01\x08\x0a\x00\x01\x06\x01\x02\x03\x04\x05\x06\x00\x00\x8e\xc6\x55'  # for user
    #           0  1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
    # # for transaction
    # buf = b'\xaa\x01\x08\x0b\x00\x05\x07\x01\x02\x03\x04\x05\x06\x07\x00\x00\xb1\xd1\x55'

    # self.zkclient.sendto(buf, self.address)
    print('zkdevicedata : flag here: ', buf)
    print('zkdevicedata : flag here length : ', len(buf))
    print('zkdevicedata :flag here hex : ', buf.hex())
    print('zkdevicedata :flag here decode : ',
          buf.decode('utf-8', errors='ignore'))
    # buf = b'\xaa\x01\x76\x04\x00\x00\x00\x01\x00\xd6\x1f\x55'
    try:
        self.zkclient.send(buf)
        self.data_recv = self.zkclient.recv(1024)
        # print("zkconnect :received data %s " % self.data_recv)

        # print("zkconnect :len(self.data_recv) %s " % len(self.data_recv))
        if len(self.data_recv) > 2:
            is_connected = self.data_recv[2] == Command.C3_CONNECT_REPLY.value

        # print("zkconnect :received => ", bytes([13]).hex())
        print("zkdevicedata :received 1 data  %s " % self.data_recv)
        print("zkdevicedata: received 2 data hex %s " % self.data_recv.hex())
        print("zkdevicedata: received 3 data Length : %s " %
              len(self.data_recv))

        print("Data => self.data_recv : ",  self.data_recv[5:-3])
        print("Data => self.data_recv Decode : ",
              self.data_recv[5:-3].decode('utf-8', errors='ignore'))
        print("Data => self.data_recv : hex : ",
              self.data_recv[5:-3].hex())
        print("Version => self.data_recv Length : ",
              len(self.data_recv[5:-3]))

        # print("zkconnect: received 3 data %s " % self.data_recv[2:3])

        # print("zkconnect: received 4 data %s " %
        #       unpack("i", self.data_recv[2:4]))

        # print("zkconnect: 8 received data hex %s " % self.data_recv[:8].hex())
        return self.data_recv
    except:
        # return False
        raise


def zkdevicename(self):
    """Start a connection with the time clock"""
    command = CMD_DEVICE
    command_string = '~DeviceName'
    chksum = 0
    session_id = self.session_id
    reply_id = unpack('HHHH', self.data_recv[:8])[3]

    buf = self.createHeader(command, chksum, session_id,
                            reply_id, command_string)
    self.zkclient.sendto(buf, self.address)
    # print (buf.encode("hex"))
    try:
        self.data_recv, addr = self.zkclient.recvfrom(1024)
        self.session_id = unpack('HHHH', self.data_recv[:8])[2]
        return self.data_recv[8:]
    except:
        return False


def zkenabledevice(self):
    """Start a connection with the time clock"""
    command = CMD_ENABLEDEVICE
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


def zkdisabledevice(self):
    """Start a connection with the time clock"""
    command = CMD_DISABLEDEVICE
    command_string = '\x00\x00'
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
