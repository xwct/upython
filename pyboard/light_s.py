# main.py -- put your code here!
from pyb import *
import os

def light():
    b = Pin('X17', Pin.IN, Pin.PULL_NONE)
    ld = ADC(Pin('X1'))
    val = ld.read()

    print(val)
