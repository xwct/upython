from pyb import ADC as adc, Pin as pin, delay, wfi, Switch
import pyb

div = 4.33/4095
i = 0
def read_tmp():
    tp = adc(pin('X2'))
    val = tp.read()
    print(val,' div ')
    mv = (val*div*1000)
    print(mv, 'mV ')
    tmp = ((val*div*1000)-500)/10
    print(tmp,'°C\n')

def tmp_loop(num):
    while True:
        read_tmp()
        delay(num)
def f():
    global i
    i = i + 1
def tmp_wfi():
    sw = Switch()
    sw.callback(f)
    global i
    while True:
        if (i == 1):
            read_tmp()
            i = 0
        else:
            pyb.wfi()
if __name__ == '__main__':
    print('bad')
