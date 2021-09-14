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
import sys
import pprint
import time
import models.zkconst
from struct import *
from models import zklib
from ast import Bytes
import codecs
from struct import pack, unpack
from .zkconst import *
from .zk_nga import *


# def buffer_connect():
#     C3_PROTOCOL_VERSION = 0x01
#     C3_COMMAND_CONNECT = 0x76

#     data = []

#     message_length = 0x04 + len(data)
#     print("message_length : ", message_length)
#     sessionID = [0x00, 0x00]
#     requestNr = 0

#     print("lsb(message_length) : ", lsb(message_length))
#     print("msb(message_length) : ", msb(message_length))

#     message = [C3_PROTOCOL_VERSION, C3_COMMAND_CONNECT, lsb(message_length),
#                msb(message_length), sessionID[1] or 0x00,
#                sessionID[0] or 0x00,
#                lsb(requestNr), msb(requestNr)]

#     if data:
#         for _, byte in enumerate(data):
#             message.append(byte)

#     print("1 - message :", message)

#     print(isinstance(message, list))

#     checksum = crc16(message)

#     print("checksum :", checksum)

#     message.append(lsb(checksum))
#     print("lsb:", lsb(checksum))
#     print("message with lsb:", message)

#     message.append(msb(checksum))
#     print("Msb:", msb(checksum))
#     print("message msb:", message)
#     message.append(0x55)
#     print("message 0x55:", message)
#     message.insert(0, 0xaa)

#     print("message last:", message)

#     message = bytes(message)
#     print("Convert to Bytes :", message)
#     print("Convert to Hex :", message.hex())
#     print("Convert to Hex Length:", len(message.hex()))

#     return message


def zkconnect(self):
    """Start a connection with the time clock"""

    #buf = create_buffer(self, Command.C3_COMMAND_CONNECT, [0x00, 0x00], )
    buf = self.nga.create_buffer(Command.C3_COMMAND_CONNECT)
    # self.zkclient.sendto(buf, self.address)
    print('after => zkconnect :flag here: ', buf)
    print('after => zkconnect :flag here hex : ', buf.hex())
    # buf = b'\xaa\x01\x76\x04\x00\x00\x00\x01\x00\xd6\x1f\x55'
    is_connected = False
    try:
        self.zkclient.connect(self.address)
        self.zkclient.send(buf)
        self.data_recv = self.zkclient.recv(1024)
        # print("zkconnect :received data %s " % self.data_recv)

        # print("zkconnect :len(self.data_recv) %s " % len(self.data_recv))
        if len(self.data_recv) > 2:
            is_connected = self.data_recv[2] == Command.C3_CONNECT_REPLY.value

        # print("zkconnect :received => ", bytes([13]).hex())
        print("zkconnect :received 1 data  %s " % self.data_recv)
        print("zkconnect: received 2 data hex %s " % self.data_recv.hex())
        # print("zkconnect: received 3 data %s " % self.data_recv[2:3])
        # print("C3_REPLY :", Command.C3_CONNECT_REPLY.value)

        # print("zkconnect: received 4 data %s " %
        #       unpack("i", self.data_recv[2:4]))

        #print("Is_Connected : ", is_connected)

        if is_connected:
            self.nga.request_number += 1
            self.session_id = [self.data_recv[6],  self.data_recv[5]]
            self.nga.nga_session_id = self.session_id
        # print("self.session_id  : ", self.session_id)
        # print("zkconnect: 8 received data %s " % self.data_recv[:8])
        # for index, byte in enumerate(self.data_recv):
        #     print("index :", index, " Value => ", byte)
        # print("zkconnect: 0 received data %s " % self.data_recv[0])
        # print("zkconnect: 1 received data %s " % self.data_recv[1])
        # print("zkconnect: 2 received data %s " % self.data_recv[2])
        # print("zkconnect: 8 received data hex %s " % self.data_recv[:8].hex())
        #print("Connection ******************************************************")

        # return self.checkValid(self.data_recv)
        return is_connected
    except:
        # return False
        raise


def zkdisconnect(self):
    """Disconnect from the clock"""

    #buf = create_buffer(self, Command.C3_COMMAND_CONNECT, [0x00, 0x00], )
    buf = self.nga.create_buffer(Command.C3_COMMAND_DISCONNECT)
    # self.zkclient.sendto(buf, self.address)
    # print('after => zkconnect :flag here: ', buf)
    # print('after => zkconnect :flag here hex : ', buf.hex())
    # buf = b'\xaa\x01\x76\x04\x00\x00\x00\x01\x00\xd6\x1f\x55'
    is_disconnected = False
    try:
        # self.zkclient.connect(self.address)
        self.zkclient.send(buf)
        self.data_recv = self.zkclient.recv(1024)
        # print("zkconnect :received data %s " % self.data_recv)

        # print("zkconnect :len(self.data_recv) %s " % len(self.data_recv))

        if len(self.data_recv) > 2:
            is_disconnected = self.data_recv[2] == Command.C3_DISCONNECT_REPLY.value
        print("zkdisconnect: received data %s " % self.data_recv)

        if is_disconnected:
            self.zkclient.close()
        # print("zkconnect :received data hex  %s " % self.data_recv.hex())
        #print("Is_Connected : ", is_connected)

        # return self.checkValid(self.data_recv)

        self.session_id = None
        self.nga.nga_session_id = None
        self.nga.request_number = 0

        return is_disconnected
    except:
        # return False
        raise


def zkconnect1(self):
    """Start a connection with the time clock"""
    command = CMD_CONNECT
    command_string = ''
    chksum = 0
    session_id = 0
    reply_id = -1 + USHRT_MAX

    buf = self.createHeader(command, chksum, session_id,
                            reply_id, command_string)

    self.zkclient.sendto(buf, self.address)

    try:
        self.data_recv, addr = self.zkclient.recvfrom(1024)
        self.session_id = unpack('HHHH', self.data_recv[:8])[2]

        return self.checkValid(self.data_recv)
    except:
        return False


def zkdisconnect1(self):
    """Disconnect from the clock"""
    command = CMD_EXIT
    command_string = ''
    chksum = 0
    session_id = self.session_id

    reply_id = unpack('HHHH', self.data_recv[:8])[3]

    buf = self.createHeader(command, chksum, session_id,
                            reply_id, command_string)

    self.zkclient.sendto(buf, self.address)

    self.data_recv, addr = self.zkclient.recvfrom(1024)
    return self.checkValid(self.data_recv)
