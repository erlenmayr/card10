# display animated Swiss style clockwork
# https://github.com/erlenmayr/card10
# contact: verbuecheln@posteo.de
# License: GPLv2

import color
import display
import math
import utime
import htmlcolor
import os
import power



def draw_teeth(disp, x, y, radius, ang, col, s):
    for i in range(round(2.1 * radius)):
        tang = ang + i * 3 / radius
        x1 = x - round(radius * math.sin(tang))
        y1 = y - round(radius * math.cos(tang))
        x2 = x - round((radius + 1) * math.sin(tang))
        y2 = y - round((radius + 1) * math.cos(tang))
        disp.line(x1, y1, x2, y2, col=col, size=s)



def draw_gear(disp, x, y, radius, ang, col, *, teeth=True):
    xd = round((radius - 5) * math.sin(ang))
    yd = round((radius - 5) * math.cos(ang))
    if teeth:
        draw_teeth(disp, x, y, radius, ang, color.BLACK, 2)
    disp.line(x + xd, y + yd, x - xd, y - yd, col=color.BLACK, size=5)
    disp.circ(x, y, radius - 6, col=col, filled=False, size=6)
    disp.circ(x, y, radius - 6, col=color.BLACK, filled=False)
    disp.line(x + xd, y + yd, x - xd, y - yd, col=col, size=4)
    if teeth:
        draw_teeth(disp, x, y, radius, ang, col, 1)



def draw_hand(disp, x, y, len, ang, col, thick):
    xs = x - round(len * math.sin(ang))
    ys = y - round(len * math.cos(ang))
    disp.line(x, y, xs, ys, col=color.BLACK, size=thick+1)
    disp.line(x, y, xs, ys, col=col, size=thick)



# draws a spring that indicates battery charge
def draw_spring(disp, charge):
    disp.rect(0, 0, 9, 19, col=htmlcolor.DIMGRAY)
    disp.rect(10, 5, 99, 14, col=htmlcolor.DARKRED)
    disp.rect(100, 5, 159, 14, col=htmlcolor.DARKGREEN)
    p = round(90 - 60 * charge)
    disp.rect(10 + p, 0, 80 + p, 20, col=htmlcolor.BLACK)
    disp.rect(11 + p, 1, 79 + p, 19, col=htmlcolor.DIMGRAY)
    for i in range(6):
        f = 10 + round((2 * i + 1)     * (p / 12.0))
        g = 10 + round((2 * i + 2) * (p / 12.0))
        disp.line(f, 2, g, 18, col=htmlcolor.BLACK, size=2)
        disp.line(f, 2, g, 18, col=htmlcolor.DIMGRAY)



def draw_gears(disp, t, ms):
    # pendel
    draw_gear(disp, 90, 39, 50, 1.570796 - 1.047198  * math.sin(0.006283185 * ms), htmlcolor.DARKGOLDENROD, teeth=False)
    # minute gears
    draw_gear(disp, 80, 40, 35, t[4] * -0.1047198, htmlcolor.DIMGRAY)
    draw_gear(disp, 136, 50, 20, t[4] * 0.3665192, htmlcolor.DIMGRAY)
    # second gears
    draw_gear(disp, 80, 40, 15, t[5] * -0.1047198, htmlcolor.DIMGRAY)
    draw_gear(disp, 33, 46, 30, t[5] * 0.05235988, htmlcolor.DIMGRAY)



def draw_hands(disp, t):
    # hour hand
    draw_hand(disp, 80, 40, 20, (t[3] + t[4] / 60.0) * -0.5235988, htmlcolor.GOLD, 2)
    # minute hand
    draw_hand(disp, 80, 40, 30, t[4] * -0.1047198, htmlcolor.GOLD, 2)
    # second hand
    draw_hand(disp, 80, 40, 35, t[5] * -0.1047198, htmlcolor.ORANGERED, 1)
    disp.circ(80, 40, 4, col=color.BLACK, filled=True, size=1)
    disp.circ(80, 40, 3, col=htmlcolor.ORANGERED, filled=True, size=1)



def animate():
    with display.open() as disp:
        while True:
            t = utime.localtime()
            ms = utime.time_ms() % 1000
            disp.clear()
            volt = os.read_battery()
            charge = (volt - 3.4) / 0.8
            t0 = utime.time_ms()
            draw_spring(disp, charge)
            draw_gears(disp, t, ms)
            draw_hands(disp, t)
            t1 = utime.time_ms()
            disp.update()
            disp.print(str(t1-t0), posx=100, posy=60)
            disp.update()



animate()

