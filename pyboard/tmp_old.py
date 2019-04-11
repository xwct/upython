from pyb import ADC as adc, Pin as pin, delay, wfi, Switch
import pyb

i = 0
def print_tmp():
    tp = adc(pin('X22'))
    val = tp.read()
    print(val,' div ')
    #mv = (val*div)
    print(mv, 'mV ')
    #tmp = (val/4095)*3.3*100#-50 #close but no cigar
    tmp = val*(3300/4096)
    print(tmp/10, ' °C\n ')

def print_mv():
    tp = adc(pin('X22'))
    val = tp.read()


def read_tmp():
    tp = adc(pin('X22'))
    val = tp.read()
    tmp = (val/4095)*3.3*100#-50 #close but no cigar
    return tmp

def tmp_loop(num):
    sw = Switch()
    state = sw()
    while not state:
        print_tmp()
        delay(num)
	state = sw()

def f():
    global i
    i = i + 1

def tmp_wfi():
    sw = Switch()
    sw.callback(f)
    global i
    while True:
        if (i == 1):
            print_tmp()
            i = 0
        else:
            pyb.wfi()

def avg(num):
    tot = 0.0
    read_tmp() #trash first reading
    for i in range(num):
        tot = tot + read_tmp()
        delay(10)
    avg_tmp = tot/num
    print(avg_tmp, '°C\n')

def tmp_loop_avg(num, wait):
    temps = [0] * num
    sw = Switch()
    state = sw()
    read_tmp()
    while not state:
        for i in range(num):
	    temps.insert(0, read_tmp())
	    temps.pop()
	    delay(wait)
	tot = sum(temps)
	avg = tot/num
	print(avg, '°C average over ', num, ' readings.\n')
	delay(1000)
	state = sw()
