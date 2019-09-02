import bhi160
import display
import utime
import color
import math

def draw_needle(disp, x, y, angle):
    rangle = math.radians(angle)
    sangle = math.radians(angle + 90)
    xf = round(20 * math.sin(rangle))
    yf = round(20 * math.cos(rangle))
    xs = round(3 * math.sin(sangle))
    ys = round(3 * math.cos(sangle))
    disp.line(x-xf, y-yf, x+xs, y+ys, col=color.RED, size=2)
    disp.line(x-xf, y-yf, x-xs, y-ys, col=color.RED, size=2)
    disp.line(x+xf, y+yf, x+xs, y+ys, col=color.WHITE, size=2)
    disp.line(x+xf, y+yf, x-xs, y-ys, col=color.WHITE, size=2)



def draw_scale(disp, x, y):
    for i in range(16):
        len = 1
        if i % 4 == 0:
            len = 3
        x1 = x - round(30 * math.sin(i * 6.283185 / 16))
        y1 = y - round(30 * math.cos(i * 6.283185 / 16))
        x2 = x - round((30 + len) * math.sin(i * 6.283185 / 16))
        y2 = y - round((30 + len) * math.cos(i * 6.283185 / 16)) 
        disp.line(x1, y1, x2, y2, col=color.WHITE)
        disp.print("N", posx=80, posy=0, font=display.FONT12)
        disp.print("E", posx=40, posy=40, font=display.FONT12)
        disp.print("S", posx=80, posy=72, font=display.FONT12)
        disp.print("W", posx=120, posy=40, font=display.FONT12)



def compass():
    disp = display.open()
    sensor = bhi160.BHI160Orientation()
    while True:
        samples = sensor.read()
        if len(samples) > 0:
            disp.clear()
            sample = samples[0]
            draw_scale(disp, 80, 40)
            draw_needle(disp, 80, 40, sample.x)
            disp.update()
        utime.sleep(0.1)



compass()

