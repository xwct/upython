# main.py -- put your code here!

import pyb

def f():
    i = 1

pyb.LED(4).on()

sw = pyb.switch()
sw.callback(f)

while True:
    if (i == 0):
        i = 0


