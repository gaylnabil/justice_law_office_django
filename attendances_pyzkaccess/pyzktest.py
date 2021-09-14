
from models.zkteco import *
from pyzkaccess import ZKAccess
import math
import ctypes
import time
from datetime import datetime
# from openpyxl import Workbook
from threading import Thread
from psycopg2 import *
from pickle import dump
from cryptography.fernet import Fernet


connstr = 'protocol=TCP,ipaddress=10.220.1.5,port=4370,timeout=4000,passwd='
zk = ZKAccess(connstr=connstr)
# print("zk.connect :", zk.connect)
print("zk.connect :", zk.sdk.is_connected)

# zk.sdk.is_connected = False

if zk.sdk.is_connected:
    # create()
    print("****************************************************")
    print('Device SN:', zk.parameters.serial_number,
          '\nIP:', zk.parameters.ip_address)
    time.sleep(1)

    # table = 'user'
    # field_name = '*'
    # pfilter = ''
    # options = ''

    # query_buf = ctypes.create_string_buffer(4 * math.pow(1024, 2))
    # query_table = ctypes.create_string_buffer(table)
    # query_field_name = ctypes.create_string_buffer(field_name)
    # query_pfilter = ctypes.create_string_buffer(pfilter)
    # query_options = ctypes.create_string_buffer(options)
    # ret = zk.dll.get

    # query_buf = ctypes.create_string_buffer(2048)
    # items = "MAC,IPAddress"
    # items = items.encode()

    # ret = zk.sdk.dll.GetDeviceParam(zk.sdk.handle, query_buf, 2048, items)

    # print("GetDeviceParam : ", ret)
    # print("query_buf : ", query_buf.value)

    print("- Ready for getting Device Data ****************************************************")
    connection = db_connect()
    # v = get_last(connection)
    # print('v : ', v)
    # seconds = 0
    # if v:
    #     print("Type: ", type(v[7]))
    #     date = v[7].replace(tzinfo=None)
    #     duration = date - datetime(2000, 1, 1, 0, 0, 0)
    #     seconds = int(duration.total_seconds())

    #     print("Get Last Attendance : ", duration)
    #     print("Get Last Attendance : ", v[7], "seconds : ", seconds)
    # time.sleep(1)

    print("- Data synchronizing ...")
    table = 'transaction'
    field_name = '*'
    pFilter = ''
    options = ''
    buffer_size = 4 * int(math.pow(1024, 2))
    query_buf = ctypes.create_string_buffer(buffer_size)
    query_table = table.encode()
    query_field_name = field_name.encode()
    query_pFilter = pFilter.encode()
    query_options = options.encode()

    ret = zk.sdk.dll.GetDeviceData(zk.sdk.handle,
                                   query_buf,
                                   buffer_size,
                                   query_table,
                                   query_field_name,
                                   query_pFilter,
                                   query_options
                                   )

    connection = db_connect()

    #print("is_connected : ", ret)
    if ret >= 0:

        #print("GetDeviceData : ", ret)

        #print("Length :", len(query_buf.value.decode().split('\r\n')))
        # count = count_attendance(connection)[0] - 2
        count = count_attendance(connection)[0]
        #print("count_attendance : ", count)

        # print("Data : ", query_buf.value[:300])

        my_thread = Thread(target=save_data, args=(
            connection, query_buf.value, count))
        my_thread.start()
