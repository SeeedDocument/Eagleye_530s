#!/usr/bin/python

import time
import sys

print "Toggle a button"
buttonpin = 54

#export pin 8 by opening file and writing the pin number to it
pinctl = open("/sys/class/gpio/export", "wb", 0)
try:
    pinctl.write( str(buttonpin))
    print "Exported pin", str(buttonpin)
except:
    print "Pin ", str(buttonpin), " has been exported"
pinctl.close()

#set pin to be digital input
filename = '/sys/class/gpio/gpio%d/direction' % buttonpin
pinctldir = open(filename, "wb", 0)
try:
    pinctldir.write("in")
    print "Set pin ", str(buttonpin), " as digital input"
except:
    print "Failed to set pin direction"
pinctldir.close()

def exit_gpio():
    #unexport pin
    pinctl = open("/sys/class/gpio/unexport", "wb", 0)
    try:
        pinctl.write( str(buttonpin))
        print "Unexported pin", str(buttonpin)
    except:
        print "Pin ", str(buttonpin), " has been unexported"
    pinctl.close()

#pin value changes when the button is pressed
filename = '/sys/class/gpio/gpio%d/value' % buttonpin
while True:
    try:
        pin = open(filename, "rb", 0)
        print pin.read()
        time.sleep(1)
        pin.close()
    except KeyboardInterrupt:
        exit_gpio()
        sys.exit(0)