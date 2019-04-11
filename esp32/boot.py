# boot.py -- runs on boot-up
# Let's you choose which script to run.
# > To run 'datalogger.py':
#       * press reset and do nothing else
# > To run 'cardreader.py':
#       * press reset
#       * press user switch and hold until orange LED goes out

import time
import machine

machine.Pin(2).on()                 # indicate we are waiting for switch press
time.sleep(2)                 # wait for user to maybe press the switch
switch_value = machine.Pin(0).value()   # sample the switch at end of delay
machine.Pin(2).off()                # indicate that we finished waiting for the switch

if switch_value:
    pyb.usb_mode('VCP+MSC')
#    pyb.main('cardreader.py')           # if switch was pressed, run this
else:
    pyb.usb_mode('VCP+HID')
#    pyb.main('datalogger.py')           # if switch wasn't pressed, run this
