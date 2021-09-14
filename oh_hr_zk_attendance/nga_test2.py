from array import array
from enum import Enum, auto, unique


@unique
class Command(Enum):

    # Protocol commands
    C3_MESSAGE_START = 0xAA
    C3_MESSAGE_END = 0x55
    C3_PROTOCOL_VERSION = 0x01
    C3_COMMAND_CONNECT = 0x76
    C3_COMMAND_DISCONNECT = 0x02
    C3_COMMAND_CONTROL = 0x05
    C3_COMMAND_GETPARAM = 0x04
    C3_COMMAND_DATATABLECFG = 0x06
    C3_COMMAND_RTLOG = 0x0B
    C3_REPLY = 0xC9  # 0xC9 instead of  0xC8
    C3_TEST = auto()


#serial_number = "~SerialNumber,LockCount,ReaderCount,AuxInCount,AuxOutCount,DateTime".encode()
serial_number = "~SerialNumber".encode()
binary = array("B", serial_number)
print("binary : ", binary)

print(" index 01 : ",
      binary[0], " => serial_number : ", serial_number)
data = binary


my_str = "~SerialNumber"
arr = bytes(my_str, 'utf-8')

for i, value in enumerate(arr):
    print("i = ", i, "; Value = ", value)

print("C3_TEST : ", Command.C3_TEST.value)
