from pyzkaccess import ZKAccess

connstr = 'protocol=TCP,ipaddress=10.220.1.5,port=4370,timeout=4000,passwd='
zk = ZKAccess(connstr=connstr)
print(zk.connect)
print('Device SN:', zk.parameters.serial_number, 'IP:', zk.parameters.ip_address)
