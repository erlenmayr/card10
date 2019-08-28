

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
    disp.print("{:.2f}V".format(volt), posx=0, posy=60)


def print_power(disp):
    pwr = power.read_battery_voltage() * power.read_battery_current() * 1000
    disp.print("{:.0f}mW".format(pwr), posx=80, posy=60)

