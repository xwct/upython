import pyb
from contextlib importcontextmanager
import os

def button(int x, str pull):
    pull.lower()
    if pull == 'none':
        pull = Pin.PULL_NONE
    elif pull == 'up':
        pull = Pin.PULL_UP
    elif pull == 'down':
        pull = Pin.PULL_DOWN
    
    b = pyb.Pin(x, pull)
    return pull



def led_ob():
    led = []
    while i < 4:
        led[i] = pub.LED(i)
    return led


@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)
    
