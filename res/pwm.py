#!/usr/bin/python

import time
import sys

print "Blink an LED"
ledpin = 159 # Blink the blue led, please change to 43 for red led

#export GPIO pin by opening file and writing the pin number to it
pinctl = open("/sys/class/gpio/export", "wb", 0)
try:
    pinctl.write( str(ledpin))
    print "Exported pin", str(ledpin)
except:
    print "Pin ", str(ledpin), " has been exported"
pinctl.close()

#set GPIO pin to be digital output
filename = '/sys/class/gpio/gpio%d/direction' % ledpin
pinctldir = open(filename, "wb", 0)
try:
    pinctldir.write("out")
    print "Set pin ", str(ledpin), " as digital output"
except:
    print "Failed to set pin direction"
pinctldir.close()

#unexport GPIO pin when we are done
def exit_gpio():
    pinctl = open("/sys/class/gpio/unexport", "wb", 0)
    try:
        pinctl.write( str(ledpin))
        print "Unexported pin", str(ledpin)
    except:
        print "Pin ", str(ledpin), " has been unexported"
    pinctl.close()

#change GPIO pin value every 10 seconds
filename = '/sys/class/gpio/gpio%d/value' % ledpin
while True:
    try:
        pin = open(filename, "wb", 0)
        pin.write( str(1) )
        time.sleep(1)

        pin.write( str(0) )
        time.sleep(1)
        pin.close()
    except:
        exit_gpio()
        sys.exit(0)
