import pyb

def face_up():
    accel = pyb.Accel()
    light = pyb.LED(3)
    SENSITIVITY = 3

    while True:
        x = accel.x()
        if abs(x) > SENSITIVITY:
            light.on()
        else:
            light.off()

        pyb.delay(100)

def spirit():
    xlights = (pyb.LED(2), pyb.LED(3))
    ylights = (pyb.LED(1), pyb.LED(4))

    accel = pyb.Accel()
    SENSITIVITY = 3

    while True:
        x = accel.x()
        if x > SENSITIVITY:
            xlights[0].on()
            xlights[1].off()
        elif x < -SENSITIVITY:
            xlights[1].on()
            xlights[0].off()
        else:
            xlights[0].off()
            xlights[1].off()

        y = accel.y()
        if y > SENSITIVITY:
            ylights[0].on()
            ylights[1].off()
        elif y < -SENSITIVITY:
            ylights[1].on()
            ylights[0].off()
        else:
            ylights[0].off()
            ylights[1].off()

        pyb.delay(100)
