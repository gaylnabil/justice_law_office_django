from models.zk_nga import Command
from struct import pack, unpack
from array import array
from .zkconst import *
# from .nga import *

# All Parameters :
# [ '~SerialNumber', '~DeviceName','AntiPassback', 'AuxInCount', 'AuxOutCount', 'BackupTime',
# 'ComPwd', 'DateTime', 'DaylightSavingTime', 'DaylightSavingTimeOn', 'DLSTMode',
# 'Door{N}CancelKeepOpenDay,' 'Door{N}CloseAndLock', 'Door{N}Detectortime',
# 'Door{N}Drivertime', 'Door{N}FirstCardOpenDoor', 'Door{N}ForcePassWord',
# 'Door{N}Intertime', 'Door{N}KeepOpenTimeZone', 'Door{N}MultiCardOpenDoor',
# 'Door{N}SensorType', 'Door{N}SupperPassWord', 'Door{N}ValidTZ',
# 'Door{N}VerifyType', 'GATEIPAddress', 'InBIOTowWay' , 'InterLock', 'IPAddress',,'MAC'
# 'LockCount', 'NetMask', 'ReaderCount', 'Reboot', 'RS232BaudRate', 'StandardTime',
# 'WatchDog', 'WeekOfMonth{N}' ,'~Platform',  '~PIN2Width', 'WorkCode']


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
    # print("Version => session_id : ", session_id)
    # reply_id = unpack('HHHH', self.data_recv[:8])[3]
    # test = unpack('HHHH', self.data_recv[:8])[0]

    # print("Version => test : ", test)
    # print("Version => self.data_recv: ", self.data_recv)
    # print("Version => self.data_recv.hex(): ", self.data_recv.hex())
    # print("Version => self.data_recv[:8] : ", self.data_recv[:8])
    # print("Version => self.data_recv[:8].hex() : ", self.data_recv[:8].hex())
    # print("Version => reply_id : ", reply_id)

    # buf = self.createHeader(command, chksum, session_id,
    #                         reply_id, command_string)

    # print("Version => createHeader : ", buf)
    # print("Version => createHeader.hex() : ", buf.hex())

    # self.zkclient.sendto(buf, self.address)
    #buf = create_buffer(self)
    #parameters = ',~SerialNumber,IPAddress,AuxOutCount,DateTime'
    #parameters = ['GATEIPAddress', 'LockCount', 'ReaderCount']

    buf = self.nga.create_buffer(Command.C3_COMMAND_GETPARAM, parameters)
    print("zkparameters => Buffer  : ", buf)
    print("zkparameters => Buffer  Hex: ", buf.hex())
    # self.zkclient.connect(self.address)
    self.zkclient.sendall(buf)
    self.data_recv = self.zkclient.recv(1024)
    self.nga.request_number += 1

    self.session_id = [self.data_recv[6],  self.data_recv[5]]
    self.nga.nga_session_id = self.session_id

    # print("Version => self.data_recv Length : ", len(self.data_recv))
    print("zkparameters => self.data_recv : ", self.data_recv)
    print("zkparameters => self.data_recv hex : ", self.data_recv.hex())
    #print("Version => self.data_recv .hex(): ", self.data_recv.hex())

    # print("self.session_id  : ", self.session_id)
    # print("Version: 8 received data %s " % self.data_recv[7:])
    # data = [byte for index, byte in enumerate(self.data_recv)]

    # print("Data : ", data)
    # data = bytes(data)
    # print("Data BYTES : ", data)
    #print("Data hex : ", data.hex())
    # for index, byte in enumerate(self.data_recv):
    #     print("index :", index, " Value => ", byte)

    # print("Version: 0 received data %s " % self.data_recv[0])
    # print("Version: 1 received data %s " % self.data_recv[1])
    # print("Version: Unpack : %s " % unpack('H', self.data_recv[2:4]))
    # print("Version: 2 received data %s " % self.data_recv[2])
    # print("Version: 8 received data hex %s " % self.data_recv[:8].hex())
    # print("Unpack :", unpack('HHHH', self.data_recv[:8]))
    #print("Version =>  self.data_recv[7:-3] : ",  self.data_recv[7:-3])
    # print("Version =>  self.data_recv[1:3] : ",  self.data_recv[3:4].hex())
    try:
        # self.data_recv, addr = self.zkclient.recvfrom(1024)
        # self.session_id = unpack('HHHH', self.data_recv[:8])[2]
        return self.data_recv[10:-3]
    except:
        return False
