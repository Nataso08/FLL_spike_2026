# FAVRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRERRRRRRRRRRRRRRETTOO
from  func import *

def M3 ():

    stopwatch = StopWatch()
    clockTime = 1000
    print(hub.battery.voltage(), " mV")

    motorTopL.reset_angle()
    resetImu()

    motorTopR.run_target(1000, 1200, Stop.HOLD, False)  # sollevamento cremagliera

    moveToDistance(68, 70, 0, 2.5)                      # avanzamento fino a tridente -> botta avanti
    moveToDistance(19, -70, 0, 2.5)                     # arretramento                -> botta indietro
    moveToDistance(8, 40, 0, 2.5)                       # allineamento con centro tridente

    motorTopL.run_angle(1000, -1100)                    # abbasso braccio 
    wait(250)
    motorTopL.run_angle(1000, 1000)                     # alzo braccio -> raccolta tridente

    turnToAngle(20, 0, 35, 2.5)                         # rotazione

    moveToDistance(10, 40, 35, 2.5)                     # avanzamento -> allineamento con missione 
    turnToAngle(0, 15, -45, 2.5)                        # rotazione verso missione

    motorTopR.run_target(1100, 340)                     # abbassamento cremagliera
    moveToDistance(9, 35, -40, 2.5)                     # ingroppamento missione
    motorTopR.run_target(1000, 1200)                    # sollevamento cremagliera -> raccolta pezzo
    
    moveToDistance(10, -60, -45, 2.5)                   # breve arretramento
    turnToAngle(0, -20, 29, 2.5)                        # rotazione verso base
    moveToDistance(75, -78, 20, 2.5)                    # ritorno in base
   
    print("M3 - Tempo impiegato: ", float(stopwatch.time())/1000, " secondi")

M3 ()
#tempo = 18sec