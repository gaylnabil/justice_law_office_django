from array import array
from struct import *


CRC_START_16 = 0x0000
CRC_POLY_16 = 0xA001
VALUE_8_BIT = 0x00FF
VALUE_32_BIT = 0xFFFF
VALUE_16_BIT = 0xFF


def lsb(value):
    return value & VALUE_8_BIT


def msb(value):
    return (value >> 8)


def calc_divisor(byte):
    poly = 0

    for _ in range(0, 8):

        if ((poly ^ byte) & 0x0001) == 1:
            #rshift = poly >> 1
            poly = (poly >> 1) ^ CRC_POLY_16
        else:
            poly = poly >> 1

        byte = byte >> 1

    return poly  # bit.band(poly, 0xFFFF) - - Truncate to 16bit


def crc16_byte(byte, crc):

    #print("before crc16_byte : ", crc)
    crc = crc & VALUE_32_BIT  # - - Truncate to 16bit
    print("crc16_byte : ", crc)
    # print("*********************************************")
    msb = crc >> 8  # Take msb from 16bit crc
    print("msb crc16_byte : ", msb)
    print("crc ^ byte crc16_byte : ", (crc ^ byte))

    crc_div = calc_divisor(crc ^ byte)
    print("crc_div crc16_byte : ", msb)
    crc = msb ^ crc_div

    return crc  # bit.band(crc, 0xFFFF)


def crc16_byte_array(byte_array, crc=None):
    crc = crc or CRC_START_16
    #print("crc16_byte_array : ", crc)
    for index, byte in enumerate(byte_array):
        print(f"before crc16_byte_array {index}: ", byte, " => ", crc)
        crc = crc16_byte(byte, crc)
        print(f"after crc16_byte_array {index}: ", byte, " => ", crc)
        print(
            "*****************************************************************************")
    return crc


def crc16_string(str, crc):
    crc = crc or CRC_START_16
    array = bytes(str)
    for value in array:
        crc = crc16_byte(value, crc)
    return crc


def crc16(data, crc=0):

    if isinstance(data, str):
        return crc16_string(data, crc)
    elif isinstance(data, list):
        return crc16_byte_array(data, crc)

    else:
        return crc16_byte(data, crc)

# # message to send to device ****************************************************


C3_PROTOCOL_VERSION = 0x01
C3_COMMAND_CONNECT = 0x76

data = []

message_length = 0x04 + len(data)
print("message_length : ", message_length)
sessionID = [0x00, 0x00]
requestNr = 0

print("lsb(message_length) : ", lsb(message_length))
print("msb(message_length) : ", msb(message_length))

message = [C3_PROTOCOL_VERSION, C3_COMMAND_CONNECT, lsb(message_length),
           msb(message_length), sessionID[1] or 0x00,
           sessionID[0] or 0x00,
           lsb(requestNr), msb(requestNr)]

if data:
    for _, byte in enumerate(data):
        message.append(byte)


print("1 - message :", message)

print(isinstance(message, list))

checksum = crc16(message)

print("checksum :", checksum)

message.append(lsb(checksum))
print("lsb:", lsb(checksum))
print("message with lsb:", message)

message.append(msb(checksum))
print("Msb:", msb(checksum))
print("message msb:", message)
message.append(0x55)
print("message 0x55:", message)
message.insert(0, 0xaa)

print("message last:", message)

message = bytes(message)
print("Convert to Bytes :", message)
print("Convert to Hex :", message.hex())
print("Convert to Hex Length:", len(message.hex()))

buf = b'\xaa\x01\x76\x04\x00\x00\x00\x01\x00\xd6\x1f\x55'
print('zkconnect : flag here: ', buf)
print('zkconnect : flag here hex : ', buf.hex())
print("zkconnect : flag here hex Length:", len(message.hex()))

# data = [1, 2]
# print(type(data))

# print(isinstance(data, list))


# data = "Good Job"
# print(type(data))

# print(isinstance(data, str))
m = 1
print(str(m) + " rshift ==> " + str(m << 8))

for i in range(0, 8):
    print(i)
