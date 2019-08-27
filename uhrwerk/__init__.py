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



def draw_gear(disp, x, y, radius, ang, col):
    xd = round((radius - 5) * math.sin(ang))
    yd = round((radius - 5) * math.cos(ang))
    disp.line(x + xd, y + yd, x - xd, y - yd, col=color.BLACK, size=5)
    disp.circ(x, y, radius - 5, col=col, filled=False, size=5)
    disp.circ(x, y, radius - 5, col=color.BLACK, filled=False)
    disp.circ(x, y, radius, col=color.BLACK, filled=False)
    disp.line(x + xd, y + yd, x - xd, y - yd, col=col, size=4)



def draw_hand(disp, x, y, len, ang, col, thick):
    xs = x - round(len * math.sin(ang))
    ys = y - round(len * math.cos(ang))
    disp.line(x, y, xs, ys, col=color.BLACK, size=thick+1)
    disp.line(x, y, xs, ys, col=col, size=thick)



def draw_battery(disp):
    volt = os.read_battery()
    perc = (volt - 3.4) / 0.8
    fill = min(19, round(perc * 20))
    col = (max(0, round((1 - perc) * 255)), 255, 0)
    if perc < 0.5:
        col = (255, min(255, round(perc * 255)), 0)
    if perc > 1.0:
        col = (0, 0, 255)
    disp.rect(0, 0, 23, 10, col=color.WHITE, filled=True, size=1)
    disp.rect(1, 1, 22, 9, col=color.BLACK, filled=True, size=1)
    disp.rect(2, 2, 2 + fill, 8, col=col, filled=True, size=1)
    disp.rect(24, 3, 25, 6, col=color.WHITE, filled=True, size=1)



def print_voltage(disp):
    volt = os.read_battery()
    disp.print(("%.2f" % volt) + "V")



def print_power(disp):
    mW = power.read_battery_voltage() * power.read_battery_current() * 1000
    disp.print(("%.1f" % mW) + "mW")



def draw_gears(disp, t, ms):
    # pendel
    draw_gear(disp, 100, 39, 60, 1.570796 - 0.7853982 * math.sin(0.006283185 * ms), htmlcolor.DIMGRAY)
    # minute gears
    draw_gear(disp, 80, 40, 35, t[4] * -0.1047198, htmlcolor.DIMGRAY)
    draw_gear(disp, 133, 50, 20, t[4] * 0.3665192, htmlcolor.DIMGRAY)
    # second gears
    draw_gear(disp, 80, 40, 15, t[5] * -0.1047198, htmlcolor.DIMGRAY)
    draw_gear(disp, 38, 54, 30, t[5] * 0.05235988, htmlcolor.DIMGRAY)



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
            check_buttons()
            disp.clear()
            draw_gears(disp, t, ms)
            draw_hands(disp, t)
            draw_battery(disp)
            disp.update()
            utime.sleep_ms(50)



animate()

