import keyboard
from models import zklib
from struct import *
import sys
import time

sys.path.append("models")

print('Connecting to Device .....')
print()
while True:

    zk = zklib.ZKLib("10.220.1.5", 4370)

    ret = zk.connect()

    if ret:

        print('- Device mode : Connected.')
        print()
        print('- Start Getting the real time Log ....')
        print()

        attendance = zk.getAttendance()

        is_disconnect = zk.disconnect()
        if is_disconnect:
            print()
            print('- Device mode : Disconnect.')

    print()
    print('Waiting for reconnecting to Device .....')
    print()
    time.sleep(5)

    if keyboard.is_pressed('s' or 'S'):
        print('Close and Exit ....')
        break
