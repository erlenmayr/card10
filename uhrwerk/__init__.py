import color
import display
import math
import utime
import htmlcolor
import os
import power




class Gear:
    def __init__(self, disp, x, y, radius, col, velo):
        self.disp = disp
        self.x = x
        self.y = y
        self.radius = radius
        self.col = col
        self.ang = 0
        self.velo = velo
    def turn(self, units):
        self.ang = math.radians(units * self.velo)
    def pendel(self, ms):
        self.ang = math.radians(90) - math.radians(45) * math.sin(math.radians(0.36 * ms))
    def draw(self):
        thick = 5
        xs = self.x + round((self.radius - thick) * math.sin(self.ang))
        ys = self.y + round((self.radius - thick) * math.cos(self.ang))
        xe = self.x - round((self.radius - thick) * math.sin(self.ang))
        ye = self.y - round((self.radius - thick) * math.cos(self.ang))
        self.disp.line(xs, ys, xe, ye, col=color.BLACK, dotted=False, size=thick+1)
        self.disp.circ(self.x, self.y, self.radius - thick, col=self.col,    filled=False, size=thick)
        self.disp.circ(self.x, self.y, self.radius - thick, col=color.BLACK, filled=False, size=1)
        self.disp.circ(self.x, self.y, self.radius,             col=color.BLACK, filled=False, size=1)
        self.disp.line(xs, ys, xe, ye, col=self.col,    dotted=False, size=thick)







class Hand:
    def __init__(self, disp, x, y, len, col, thick, velo):
        self.disp = disp
        self.x = x
        self.y = y
        self.len = len
        self.ang = 0
        self.thick = thick
        self.col = col
        self.velo = velo
    def turn(self, units):
        self.ang = math.radians(units * self.velo)
    def draw(self):
        xs = self.x - round(self.len * math.sin(self.ang))
        ys = self.y - round(self.len * math.cos(self.ang))
        self.disp.line(self.x, self.y, xs, ys, col=color.BLACK, dotted=False, size=(self.thick+1))
        self.disp.line(self.x, self.y, xs, ys, col=self.col, dotted=False, size=self.thick)



def print_battery(disp):
        volt = os.read_battery()
        perc = (volt - 3.4) / 0.8
        fill = min(19, round(perc * 20))
        bar = (min(255, round((1 - perc) * 255)), 255, 0)
        if perc < 0.5:
            bar = (255, min(255, round(perc * 255)), 0)
        disp.rect(0, 0, 23, 10, col=color.WHITE, filled=True, size=1)
        disp.rect(1, 1, 22, 9, col=color.BLACK, filled=True, size=1)
        disp.rect(2, 2, 2 + fill, 8, col=bar, filled=True, size=1)
        disp.rect(24, 3, 25, 6, col=color.WHITE, filled=True, size=1)




def ani():
    with display.open() as disp:
        pendel = Gear(disp, 100, 39, 60, (48, 48, 48), 0)
        mg1 = Gear(disp, 80, 40, 35, (48, 48, 48), -6)
        mg2 = Gear(disp, 133, 50, 20, (48, 48, 48), 21)
        sg1 = Gear(disp, 80, 40, 15, (48, 48, 48), -6)
        sg2 = Gear(disp, 38, 54, 30, (48, 48, 48), 3)
        hh = Hand(disp, 80, 40, 20, htmlcolor.GOLD, 2, -30)
        mh = Hand(disp, 80, 40, 30, htmlcolor.GOLD, 2, -6)
        sh = Hand(disp, 80, 40, 35, htmlcolor.ORANGERED, 1, -6)
        ms = 0;
        while True:
            time = utime.localtime()
            pendel.pendel(ms)
            mg1.turn(time[4])
            mg2.turn(time[4])
            sg1.turn(time[5])
            sg2.turn(time[5])
            hh.turn(time[3] + (time[4] / 60.0))
            mh.turn(time[4])
            sh.turn(time[5])
            disp.clear()
            print_battery(disp)
            pendel.draw()
            mg1.draw()
            mg2.draw()
            sg1.draw()
            sg2.draw()
            hh.draw()
            mh.draw()
            sh.draw()
            disp.circ(80, 40, 4, col=color.BLACK, filled=True, size=1)
            disp.circ(80, 40, 3, col=htmlcolor.ORANGERED, filled=True, size=1)
            disp.update()
            ms = (utime.time_ms() % 1000)
            utime.sleep_ms(50)


ani()


