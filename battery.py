
import display
import color
import utime
import math
import leds
import buttons
import ujson
import os
import power



def print_battery(disp):
        volt = os.read_battery()
        perc = (volt - 3.4) / 0.8
        fill = min(20, round(perc * 20))
        bar = (min(255, round((1 - perc) * 255)), 255, 0)
        if perc < 0.5:
            bar = (255, min(255, round(perc * 255)), 0)
        disp.rect(147, 2, 159, 25, col=color.WHITE, filled=True, size=1)
        disp.rect(148, 3, 158, 24, col=color.BLACK, filled=True, size=1)
        disp.rect(149, 24 - fill, 157, 23, col=bar, filled=True, size=1)
        disp.rect(149, 0, 157, 2, col=color.WHITE, filled=True, size=1)

def print_voltage(disp):

def print_power(disp):
mW = round(power.read_battery_voltage() * power.read_battery_current() * 1000)
disp.print(str(mW) + "mW")


