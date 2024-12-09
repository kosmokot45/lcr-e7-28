import time
import usb.core
import usb.util

PID = 0xea60
VID = 0x10c4

dev = usb.core.find(idVendor=VID, idProduct=PID)
if not dev:
        print "CP2104 was not found :("
        exit(1)
print "Yeeha! Found CP2104"

reqType = 0x41
bReq = 0xFF
wVal = 0x37E1

while True:

        wIndex = 0xffff
        print "toggling On"
        dev.ctrl_transfer(reqType, bReq, wVal, wIndex, [])
        time.sleep(5)
        print "toggling Off"
        wIndex = 0x00ff
        dev.ctrl_transfer(reqType, bReq, wVal, wIndex, [])
        time.sleep(5)