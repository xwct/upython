import machine, time

def cycle():
    r = machine.PWM(machine.Pin(15))
    g = machine.PWM(machine.Pin(13))
    b = machine.PWM(machine.Pin(12))
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):
                for i in range(0,101):
                    r.duty(x*i)
                    g.duty(y*i)
                    b.duty(z*i)
                    time.sleep_ms(50)
