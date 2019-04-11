from ssd1306 import SSD1306
import pyb
from tmp import TMP_OLED

display = SSD1306(pinout={'sda': 'Y10',
                          'scl': 'Y9'},
		      height=64,
		      external_vcc=False)

r_led = pyb.LED(1)
r_led.off()

try:
    display.poweron()
    display.init_display()
    tmp = TMP_OLED('X22')

    display.draw_text(32, 28, "Loading", size=2, space=1)
    display.display()
    temp = tmp.tmp_loop(10,1000)
    display.clear()

    while True:
	display.draw_text(5, 10, "Temperature", size=2, space=1)
	display.draw_text(5, 30, temp, size=2, space=1)
	display.display()
	temp = tmp.tmp_loop(10,1000)

except Exception as ex:
    r_led.on()
    print('Unexpected error: {0}'.format(ex))
    display.poweroff()

except KeyboardInterrupt:
    display.clear()
    display.poweroff()
    print("Quitting...")
