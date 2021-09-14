import keyboard
from models import zklib
from struct import *
import sys
import time

sys.path.append("models")

# value = b'\x00\x01\x06'
# value = b'\x00\x02\x03'

# print(int.from_bytes(b'\xf3', byteorder='big'))
# print(int.from_bytes(b'\x13', byteorder='big'))

# print("Value decode :", value.decode(
#     'utf-8', errors='ignore'),  value.hex(),  bytes.fromhex('000203'), type(0x000203))
print('Connecting to Device .....')
print()

# while True:

zk = zklib.ZKLib("10.220.1.5", 4370)

ret = zk.connect()
print("connection:", ret, "**********************************")

if ret:

    print('- Device mode : Connected.')

    parameters = ['~DeviceName', '~SerialNumber', 'MAC', '~OS', '~Platform', 'NetMask', 'IPAddress',
                  'GATEIPAddress', 'AuxInCount', 'LockCount', 'ReaderCount', 'DLSTMode',
                  'DateTime', 'DaylightSavingTimeOn', 'Door1CloseAndLock', 'InterLock',
                  'RS232BaudRate', 'WatchDog', 'StandardTime',  '~PIN2Width', 'WorkCode']
    data = zk.parameters(parameters).decode()
    data = data.split(',')

    print("ZK Parameters: **********************************")

    for value in data:
        print(value.replace('~', ''))

    # print('- Start Getting the real time Log ....')
    # print()

    # attendance = zk.getAttendance()

    # print('attendance : ', attendance)
    # print('attendance : ', attendance.decode('utf-8', errors='ignore'))

    # zk.show()
    print("Start get DeviceData => *********************************************************************")
    C3_USER = [0x03, 0x04, 0x05, 0x06, 0x00, 0x00]

    parameters = [
        'transaction\r\nCardno,Pin,Verified,DoorID,EventType,InOutState,Time_second\r\n']

    parameters = [
        'transaction\r\nCardno,Pin\r\n']

    # parameters = [
    #     'Action=,Table=transaction,Fields=,Filter=,Options=,']

    data = zk.getDeviceData(parameters)
    print('getDeviceData : ', data.decode('utf-8', errors='ignore'))

    is_disconnect = zk.disconnect()
    if is_disconnect:
        print()
        print('- Device mode : Disconnect.')

    # print()
    # print('Waiting for reconnecting to Device .....')
    # print()
    # time.sleep(5)
    # if keyboard.is_pressed('s' or 'S'):
    #     print('Close and Exit ....')
    #     break

    # print("ZK Version:", zk.version().decode())

    # def get_fingerprint_type(id):
    #     list = [('1', 'Finger'),
    #             ('15', 'Face'),
    #             ('2', 'Type_2'),
    #             ('3', 'Password'),
    #             ('4', 'Card'),
    #             ('101', 'Unknown-101'),
    #             ('0', 'Unknown-0')
    #             ]
    #     for type_id, name in list:
    #         #print("NGA => id: %s, name: %s" % (type_id, name))
    #         if int(type_id) == id:
    #             return name
    #     return False

    # print("starting .....")
    # hex_string = "0x616263"[2:]
    # print("hex_string : ", hex_string)
    # bytes_object = bytes.fromhex(hex_string)

    # print("bytes_object : ", bytes_object)

    # ascii_string = bytes_object.decode("utf-8")

    # print('ascii_string : ', ascii_string)

    # data = attendance
    # data = data.split(',')

    # print("ZK Parameters:")

    # for value in data:
    #     print(value.replace('~', ''))

    #     print("OS Version:", zk.osversion().decode())

    #     print("Platform:", zk.platform().decode())
    #     print("Platform Version:", zk.fmVersion().decode())
    #     print("Work Code:", zk.workCode().decode())
    #     print("SSR:", zk.ssr().decode())
    #     print("Pin Width:", zk.pinWidth().decode())
    #     print("Face Function On:", zk.faceFunctionOn().decode())
    #     print("Serial Number:", zk.serialNumber().decode())
    #     print("Device Name:", zk.deviceName().decode())

    #     try:

    #         print(
    #             "Start => *********************************************************************")
    #         data_user = zk.getUser()

    #         print("Get Users:")

    #         if data_user:
    #             for uid in data_user:

    #                 if data_user[uid][2] == 14:
    #                     level = 'Admin'
    #                 else:
    #                     level = 'User'

    #                 print("[UID %d]: ID: %s, Name: %s, Level: %s, Password: %s" % (
    #                     uid, data_user[uid][0], data_user[uid][1], level, data_user[uid][3]))
    #     except:
    #         print("Error Asers => *********************************************************************")
    #         raise
    #     finally:
    #         print("Done Users => *********************************************************************")

    #     # try:

    #     #     print("Start get Attendance => *********************************************************************")
    #     attendance = zk.getAttendance()
    #     #     # test = True
    #     #     # print ("Get Attendance: " +str(test))
    #     #     #pprint.pprint(attendance)
    #     #     if (attendance):
    #     #         # print ("Get Attendance: " +str(attendance))
    #     #         print("Get Attendance Count : ", len(attendance))
    #     #         for lattendance in attendance:
    #     #             #print("attendance ID :", repr(str(lattendance[0])))
    #     #             #state = lattendance[1]
    #     #             #print("attendance State :", state)
    #     #             #print("type : ", type(state))
    #     #             # if state == 15:
    #     #             #     state = 'Check In'
    #     #             # elif state == 0:
    #     #             #     state = 'Check Out'
    #     #             # else:
    #     #             #     state = 'Undefined'
    #     #             print(type(lattendance[1]))
    #     #             finger_type = get_fingerprint_type(lattendance[1])

    #     #             # print("date %s, Time %s, ID: %s, Status: %s (%s), space : %s, Data : %s" % (
    #     #             # lattendance[2].date(), lattendance[2].time(), lattendance[0], finger_type, lattendance[1], lattendance[3], lattendance[4]))
    #     #             print("date %s, Time %s, ID: %s, Status: %s (%s), space : %s, Data : %s" % (
    #     #                 lattendance[2].date(), lattendance[2].time(), lattendance[0], finger_type, lattendance[1],
    #     #                 lattendance[3]))

    #     # except:
    #     #     print("Error Attendance => *********************************************************************")
    #     #     raise
    #     # finally:
    #     #     print("Done Attendance => *********************************************************************")

    # print("Get Time:", zk.getTime())
    # print("Enable Device", zk.enableDevice().decode())
    # print("Disconnect:", zk.disconnect())

    # pack_data = pack('iif', 6, 19, 20.55)

    # print("pack_data :", pack_data)

    # print("calcsize('i') : ", calcsize('i'))
    # print("calcsize('f') : ", calcsize('f'))
    # print("calcsize('iif') : ", calcsize('iif'))

    # original_data = unpack('iif', pack_data)

    # print("original_data :", original_data)

    # print("Nabil".encode())
    # pack_data = pack('5s4sf', "Nabil".encode('utf-8'), "GAYL".encode(), 20.55)

    # print("pack_data :", pack_data)

    # print("calcsize('s') : ", calcsize('s'))
    # print("calcsize('f') : ", calcsize('f'))
    # print("calcsize('BsBsf') : ", calcsize('BsBsf'))

    # original_data = unpack('5s4sf', pack_data)

    # print("original_data :", original_data)

    # print("************************************************")
    # value = 0x04030201

    # a = value
    # b = value >> 16
    # c = value >> 8
    # d = value

    # print("a  : ", a)
    # print(hex(a))
    # print("b  : ", b)
    # print(hex(b))
    # print("c  : ", c)
    # print("d  : ", d)

    # a = value >> 24 & 0xff
    # b = (value >> 16) & 0xff
    # c = value >> 8 & 0xff
    # d = value & 0xff

    # print("a  : ", a)
    # print("hex a : ", hex(a))
    # print("b  : ", b)
    # print("hex b : ", hex(b))
    # print("c  : ", c)
    # print("d  : ", d)

    # '0000.0100.0000.0011.0000.0010.0000.0001'
    # 0000.0100.0000.0011
    # 0000.0000.1111.1111
    # 0000.0000.0000.0011

    # 0000.0000.0001.0000

    # 0100.0000.0011.0000.0010.0000.0001

    # 0000.0000.0000.0000.0000.1111.1111

    # print('\n'.join([' ' * 10 + '*' + ' ' * 10, '\n'.join('{0}{1}{0}'.format(' ' * ((21 - c) // 2), ''.join(
    #     map(lambda i: '#' if i % 2 else 'o', range(c)))) for c in range(3, 22, 2)), ' ' * 9 + '/|\\' + ' ' * 9]))
