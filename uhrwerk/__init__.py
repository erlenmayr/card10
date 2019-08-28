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
    disp.circ(x, y, radius - 6, col=col, filled=False, size=6)
    disp.circ(x, y, radius - 6, col=color.BLACK, filled=False)
    disp.circ(x, y, radius, col=color.BLACK, filled=False)
    disp.line(x + xd, y + yd, x - xd, y - yd, col=col, size=4)



def draw_hand(disp, x, y, len, ang, col, thick):
    xs = x - round(len * math.sin(ang))
    ys = y - round(len * math.cos(ang))
    disp.line(x, y, xs, ys, col=color.BLACK, size=thick+1)
    disp.line(x, y, xs, ys, col=col, size=thick)



# draws a spring that indicates battery charge
def draw_spring(disp):
    volt = os.read_battery()
    perc = (volt - 3.4) / 0.8
    f = 14 -  min(10, round(perc * 10))
    disp.rect(10, 5, 100, 15, col=htmlcolor.DARKRED)
    disp.rect(100, 5, 160, 15, col=htmlcolor.DARKGREEN)
    disp.rect(0, 0, 10, 20, col=color.BLACK)
    disp.rect(1, 1, 9, 19, col=htmlcolor.DIMGRAY)
    for i in range(6):
        disp.line(12+f*i, 2, 12+round(0.5*f)+f*i, 18, col=color.BLACK, size=2)
        disp.line(12+f*i, 2, 12+round(0.5*f)+f*i, 18, col=htmlcolor.DIMGRAY)
    disp.rect(15+round(0.5*f)+f*i, 0, 90+f*i, 20, col=color.BLACK)
    disp.rect(16+round(0.5*f)+f*i, 0, 89+f*i, 19, col=htmlcolor.DIMGRAY)



def draw_gears(disp, t, ms):
    # pendel
    draw_gear(disp, 90, 39, 50, 1.570796 - 1.047198  * math.sin(0.006283185 * ms), htmlcolor.DARKGOLDENROD)
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
            disp.clear()
            draw_spring(disp)
            draw_gears(disp, t, ms)
            draw_hands(disp, t)
            disp.update()
            utime.sleep_ms(20)



animate()

