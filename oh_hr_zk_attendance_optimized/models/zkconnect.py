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


def zkconnect(self):
    """Start a connection with the time clock"""

    buf = self.nga.create_buffer(Command.C3_COMMAND_CONNECT)
    is_connected = False
    try:
        self.zkclient.connect(self.address)
        self.zkclient.send(buf)
        self.data_recv = self.zkclient.recv(1024)
        if len(self.data_recv) > 2:
            is_connected = self.data_recv[2] == Command.C3_CONNECT_REPLY.value

        if is_connected:
            self.nga.request_number += 1
            self.session_id = [self.data_recv[6],  self.data_recv[5]]
            self.nga.nga_session_id = self.session_id
        return is_connected
    except:
        return False


def zkdisconnect(self):
    """Disconnect from the clock"""

    buf = self.nga.create_buffer(Command.C3_COMMAND_DISCONNECT)
    is_disconnected = False
    try:
        self.zkclient.send(buf)
        self.data_recv = self.zkclient.recv(1024)

        if len(self.data_recv) > 2:
            is_disconnected = self.data_recv[2] == Command.C3_DISCONNECT_REPLY.value

        if is_disconnected:
            self.zkclient.close()

        self.session_id = None
        self.nga.nga_session_id = None
        self.nga.request_number = 0

        return is_disconnected
    except:
        return False
