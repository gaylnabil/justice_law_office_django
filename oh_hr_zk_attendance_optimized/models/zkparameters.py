from models.zk_nga import Command
from struct import pack, unpack
from array import array
from .zkconst import *
# from .nga import *


def get_header(data):
    command = None
    size = 0
    if len(data) >= 5:
        # if data[0] == b'\xaa' and data[1] == b'\x01':
        if data[0] == 170 and data[1] == 32:
            command = data[2]
            size = (data[4] * 255) + data[3]

    return command, size


def arr_to_str(bytes):
    data = ""
    if bytes:
        for v in bytes:
            if v:
                data = data + str(v)

    return data


def zkparameters(self, parameters=None):
    """Start a connection with the time clock"""
    try:
        buf = self.nga.create_buffer(Command.C3_COMMAND_GETPARAM, parameters)
        print("zkparameters => Buffer  : ", buf)
        print("zkparameters => Buffer  Hex: ", buf.hex())

        self.zkclient.sendall(buf)
        self.data_recv = self.zkclient.recv(1024)
        self.nga.request_number += 1

        self.session_id = [self.data_recv[6],  self.data_recv[5]]
        self.nga.nga_session_id = self.session_id

        print("zkparameters => self.data_recv : ", self.data_recv)
        print("zkparameters => self.data_recv hex : ", self.data_recv.hex())

        return self.data_recv[10:-3]
    except:
        return False
