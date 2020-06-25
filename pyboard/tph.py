import machine, time
from lib import bme280, lcd160cr
from pyb import LED

# constants
MEASURE_DELAY = 60000                                                          # 1 min in ms
I2C = machine.I2C(2)
SENS = bme280.BME280(i2c=I2C)
YLED = LED(3)
GLED = LED(2)
DISP = lcd160cr.LCD160CR('X')


def sensor_read():
    data = SENS.read_compensated_data()
    return (data[0]/100, data[1]/25600, data[2]/1024)                          #turn values into celcius, hPa and % RH


#csv ish thing
def write_to_file(pData):
    with open('tph','a') as f:
        f.write(",".join([str(x) for x in pData]) + "\n")
        #print("written to file")

#initiates DISPlay in x orientation
def lcd_init(DISP):
    DISP.erase()
    DISP.set_font(1,0,0,1,0)
    DISP.set_text_color(DISP.rgb(255,255,255), DISP.rgb(0, 0, 0))              #white text black background
    #DISP.touch_config(calib=False, save=False, irq=True)

def test_high_low(current, highLow):
#    print(current)
#    print("\n", type(current), type(highLow), "\n")
    if current > highLow[0]:
        highLow[0] = current
#        print("higher")
    if current < highLow[1]:
        highLow[1] = current
#        print("lower")

    return [highLow[0], highLow[1]]

def update_lcd(pData, highLowValues):
    DISP.erase()
    DISP.set_pos(64, 72)
    DISP.write('High')
    DISP.set_pos(8, 72)
    DISP.write('Low')

    #current value update
    for i in range(3):
        DISP.set_pos(8, 8 + i * 16)
        DISP.write('%4s ' % ('Temp', 'Pres', 'RHum')[i])
        if i == 0:
            s = '{:3.1f}°C'.format(pData[i])
        elif i == 1:
            s = '{:3.1f}hPa'.format(pData[i])
        elif i == 2:
            s = '{:3.1f}%'.format(pData[i])

        DISP.write(s)

    #update high/low
    for i in range(3):
#        print(pData[i])
        highLowValues[i] = test_high_low(pData[i], highLowValues[i])
#        print(highLowValues[i])
#        print("\n", type(highLowValues), "\n", type(highLowValues[i]), "\n")
        if i == 0:
            DISP.set_pos(64, 88 + i * 16)
            DISP.write('{:3.1f}°C'.format(highLowValues[i][0]))
            DISP.set_pos(8, 88 + i * 16)
            DISP.write('{:3.1f}°C'.format(highLowValues[i][1]))
        elif i == 1:
            DISP.set_pos(64, 88 + i * 16)
            DISP.write('{:3.1f}hPa'.format(highLowValues[i][0]))
            DISP.set_pos(8, 88 + i * 16)
            DISP.write('{:3.1f}hPa'.format(highLowValues[i][1]))
        elif i == 2:
            DISP.set_pos(64, 88 + i * 16)
            DISP.write('{:3.1f}%'.format(highLowValues[i][0]))
            DISP.set_pos(8, 88 + i * 16)
            DISP.write('{:3.1f}%'.format(highLowValues[i][1]))
    DISP.set_brightness(31)

for i in range(3, 0, -1):
    GLED.toggle()
    time.sleep(1)
    print(i)

highLowValues = [[-100, 100], [300, 1100], [0,100]]                            #[high, low], init to values guaranteed to be lower/higher
_ = sensor_read()                                                              # scrap first reading
values = sensor_read()
measurementTimer = time.ticks_ms()                                                           # initial timer value
lcdTimeOut = measurementTimer
lcdOn = False
lcd_init(DISP)
GLED.on()
with open('tph','a') as f:                                                     #write header
    f.write("#temperature, pressure, humidity\n")
    #print("header written")

while True:

    if (measurementTimer + MEASURE_DELAY) < time.ticks_ms():
        values = sensor_read()
        write_to_file(values)
        measurementTimer = time.ticks_ms()
        for i in range(3):
            highLowValues[i] = test_high_low(values[i], highLowValues[i])

        print(values)

    if DISP.is_touched():
        lcdValues = sensor_read()
        #test_high_low(lcdValues, highLowValues)
        update_lcd(lcdValues, highLowValues)
        lcdTimeOut = time.ticks_ms()
        lcdOn = True
        YLED.on()
        #print("lcd update")

    if ((lcdTimeOut + 20000) < time.ticks_ms()) and lcdOn:
        DISP.set_brightness(0)
        YLED.off()
        lcdOn = False
        #print("lcd off")
