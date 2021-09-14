from array import array
from struct import *
from enum import Enum, unique, auto

CRC_START_16 = 0x0000
CRC_POLY_16 = 0xA001
VALUE_8_BIT = 0x00FF
VALUE_32_BIT = 0xFFFF
VALUE_16_BIT = 0xFF


@unique
class Command(Enum):

    # Protocol commands
    C3_MESSAGE_START = 0xAA
    C3_MESSAGE_END = 0x55
    C3_PROTOCOL_VERSION = 0x01
    C3_ATTLOG = 0x0d
    C3_COMMAND_CONNECT = 0x76
    C3_COMMAND_DISCONNECT = 0x02
    C3_COMMAND_CONTROL = 0x05
    C3_COMMAND_GETPARAM = 0x04
    C3_COMMAND_DATATABLECFG = 0x06
    C3_COMMAND_RTLOG = 0x0B
    C3_DISCONNECT_REPLY = 0xC8  # 0xC9 instead of  0xC8
    C3_CONNECT_REPLY = 0xC9  # 0xC9 instead of  0xC8
    C3_COMMAND_GETDEVICEDATA = 0x08


class ZKNga:

    def __init__(self, nga_session_id):
        self.nga_session_id = nga_session_id
        self.request_number = 0

    def lsb(self, value):
        return value & VALUE_8_BIT

    def msb(self, value):
        return (value >> 8)

    def calc_divisor(self, byte):
        poly = 0
        for _ in range(0, 8):

            if ((poly ^ byte) & 0x0001) == 1:
                # rshift = poly >> 1
                poly = (poly >> 1) ^ CRC_POLY_16
            else:
                poly = poly >> 1

            byte = byte >> 1

        return poly

    def crc16_byte(self, byte, crc):

        # print("before crc16_byte : ", crc)
        crc = crc & VALUE_32_BIT  # - - Truncate to 16bit
        msb = crc >> 8

        crc_div = self.calc_divisor(crc ^ byte)
        # print("crc_div crc16_byte : ", msb)
        crc = msb ^ crc_div

        return crc  # bit.band(crc, 0xFFFF)

    def crc16_byte_array(self, byte_array, crc=None):
        crc = crc or CRC_START_16
        for index, byte in enumerate(byte_array):
            crc = self.crc16_byte(byte, crc)
        return crc

    def crc16_string(self, str, crc):
        crc = crc or CRC_START_16
        array = bytes(str)
        for value in array:
            crc = self.crc16_byte(value, crc)
        return crc

    def crc16(self, data, crc=0):

        if isinstance(data, str):
            return self.crc16_string(data, crc)
        elif isinstance(data, list):
            return self.crc16_byte_array(data, crc)

        else:
            return self.crc16_byte(data, crc)

    def create_buffer(self, command, parameters=None):
        #parameters = "~SerialNumber,LockCount,ReaderCount,AuxInCount,AuxOutCount,DateTime".encode()
        # parameters = "DeviceID".encode()
        # binary = array("B", parameters)
        # print("binary : ", binary)
        data = []
        if parameters and isinstance(parameters, list):

            if all(isinstance(element, str) for element in parameters):

                parameters = ','.join(map(str, parameters))
                # print("ZKparameters => ", parameters)
                parameters = parameters.encode('utf-8')
                data = array("B", parameters) if parameters else []

            else:
                for element in parameters:
                    data += element

        message_length = 0x04 + len(data)
        # print("self.session_id : ", self.nga_session_id)
        self.nga_session_id = [
            0x00, 0x00] if not self.nga_session_id else self.nga_session_id

        # print("lsb(message_length) : ", self.lsb(message_length))
        # print("msb(message_length) : ", self.msb(message_length))
        # print("Request_Number : ", self.request_number)

        message = [Command.C3_PROTOCOL_VERSION.value, command.value, self.lsb(message_length),
                   self.msb(message_length), self.nga_session_id[1] or 0x00,
                   self.nga_session_id[0] or 0x00,
                   self.lsb(self.request_number), self.msb(self.request_number)]

        if data:
            for index, byte in enumerate(data):
                message.append(byte)

        # print("1 - message :", message)

        # print(isinstance(message, list))

        checksum = self.crc16(message)

        # print("checksum :", checksum)

        message.append(self.lsb(checksum))
        # print("lsb:", self.lsb(checksum))
        # print("message with lsb:", message)

        message.append(self.msb(checksum))
        # print("Msb:", self.msb(checksum))
        # print("message msb:", message)
        message.append(0x55)
        # print("message 0x55:", message)
        message.insert(0, 0xaa)

        # print("message last:", message)

        message = bytes(message)
        # print("Convert to Bytes :", message)
        # print("Convert to Hex :", message.hex())
        # print("Convert to Hex Length:", len(message.hex()))

        return message
