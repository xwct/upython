import machine, sys, pyb
from lib import bme280


class BMELCD:
    def __init__(self, i2c=2):
        self.i2c = machine.I2C(i2c)
        self.sens = bme280.BME280(i2c=self.i2c)
        self.highLowValues= [[-100, 100], [300, 1100], [0, 100]]

    def sensor_read(self):
        self.data = self.sens.read_compensated_data()
        return (self.data[0]/100, self.data[1]/25600, self.data[2]/1024)

    def test_high_low(self, current, highLow):
        self.curr = current
        self.valMin, self.valMax = highLow
        if self.curr > self.valMin:
            self.valMin = self.curr
        if self.curr < self.valMax:
            self.valMax = self.curr

        return (self.valMin, self.valMax)

    def high_low(self, values):
        self.disp.set_pos(64, 72)
        self.disp.write('Low')
        self.disp.set_pos(8, 72)
        self.disp.write('High')
        self.values = values

        for j in range(3):
            self.highLowValues[j] = self.test_high_low(self.values[j], 
                                           self.highLowValues[j])

            if j == 0:
                self.disp.set_pos(8, 88 + j * 16)
                self.disp.write('{:3.1f}°C'.format(self.highLowValues[j][0]))
                self.disp.set_pos(64, 88 + j * 16)
                self.disp.write('{:3.1f}°C'.format(self.highLowValues[j][1]))

            elif j == 1:
                self.disp.set_pos(8, 88 + j * 16)
                self.disp.write('{:3.1f}hPa'.format(self.highLowValues[j][0]))
                self.disp.set_pos(64, 88 + j * 16)
                self.disp.write('{:3.1f}hPa'.format(self.highLowValues[j][1]))
            elif j == 2:
                self.disp.set_pos(8, 88 + j * 16)
                self.disp.write('{:3.1f}%'.format(self.highLowValues[j][0]))
                self.disp.set_pos(64, 88 + j * 16)
                self.disp.write('{:3.1f}%'.format(self.highLowValues[j][1]))

    def lcd(self):
        # lcd setup
        from lib import lcd160cr
        self.disp = lcd160cr.LCD160CR('X')
        self.disp.erase()
        self.disp.set_font(1, 0, 0, 1, 0)
        self.disp.set_text_color(self.disp.rgb(255, 255, 255), 
                                 self.disp.rgb(  0,   0,   0))
        
    def loop(self):
        #TODO: main display loop 
        # while loop 
        self.values = self.sensor_read()
        self.disp.erase()
        for i in range(3):
            self.disp.set_pos(8, 8 + i * 16)
            self.disp.write('%4s ' % ('Temp', 'Pres', 'RHum')[i])
            if i == 0:
                self.s = '{:3.1f}1°C'.format(self.values[i])
            elif i == 1:
                self.s = '{:3.1f}hPa'.format(self.values[i])
            elif i == 2:
                self.s = '{:3.1f}%'.format(self.values[i])
            self.disp.write(self.s)
        
        self.high_low(self.values)

if __name__ == '__main__':
    s = BMELCD(2)
    s.lcd()
    while True:
        s.loop()
        pyb.delay(6000)
