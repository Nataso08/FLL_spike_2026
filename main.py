# PROGRAMMA MENU'

# importazione uscite come funzioni da file
from M1 import M1
from M2 import M2
from M3 import M3
from M4 import M4
# from M5 import M5
# from M6 import M6
from func import *

# array of the mission
missions = [M1, M2, M3, M4]

# logo planck
logo = [
    [0, 60, 60, 0, 0],
    [100, 100, 60, 0, 0],
    [100, 100, 60, 60, 60],
    [100, 100, 100, 100, 60],
    [100, 100, 100, 100, 0]
]

hub = PrimeHub()
############### MENU ###############

# init of variables

mission = 0
exit = False
run = False

from pybricks.tools import StopWatch
durata = StopWatch()

print("Batteria: ", hub.battery.voltage(), " mV")

# time_run = durata.time()

try:
    while not exit:
        if (mission == len(missions)):
            break
        else:
            hub.display.char(str(mission+1))

        if run:
            try:
                hub.display.icon(logo)
                resetImu()
                missions[mission]()
            except SystemExit:
                run = False
                stopMotorPair()
                motorTopL.stop()
                motorTopR.stop()
                mission += 1
                continue
            
            if mission < len(missions)-1:
                mission+=1
            else:
                exit = True
            run = False

        elif Button.CENTER in hub.buttons.pressed():
            while Button.CENTER in hub.buttons.pressed():
                pass
            run = True

        elif Button.RIGHT in hub.buttons.pressed():
            mission = mission + 1 if mission < len(missions)-1 else 0
            while Button.RIGHT in hub.buttons.pressed():
                pass

        elif Button.LEFT in hub.buttons.pressed():
            mission = mission - 1 if mission > 0 else len(missions)-1
            while Button.LEFT in hub.buttons.pressed():
                pass
except SystemExit:
    pass

# print("TOTALE: ", float(durata.time())/1000, " secondi")
print("Batteria: ", hub.battery.voltage(), " mV")
