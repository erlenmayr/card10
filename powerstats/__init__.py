import display
import power
import os
import utime

def powerstats():
    with display.open() as disp:
        while True:
            volt = os.read_battery()
            curr = power.read_battery_current() * 1000
            powr = volt * curr
            perc = (volt - 3.4) / 0.8 * 100
            disp.clear()
            disp.print("{:.1f} %".format(perc), posx=0, posy=0)
            disp.print("{:.3f} V".format(volt), posx=0, posy=20)
            disp.print("{:.1f} mA".format(curr), posx=0, posy=40)
            disp.print("{:.1f} mW".format(powr), posx=0, posy=60)
            disp.update()
            utime.sleep(1)

powerstats()

