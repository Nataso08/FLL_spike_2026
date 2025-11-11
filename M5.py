# Miniera
from func import *

def M5 ():
    stopwatch = StopWatch()
    clockTime = 1000

    resetImu()
    calibImu(2)

    motorTopL.run_angle(1000, 650, Stop.BRAKE, False)   # sollevamento cremagliera
    moveToDistance(73, 60, 0, 2.5, False)               # avanzamento
    moveToDistance(12, 35, 0, 2.5)                      # avanzamento lento
    turnToAngle(19, 0, 65, 2.5)                         # rotazione 1
    moveToDistance(14, 40, 65, 2.5)                     # avanzamento -> allineamento con miniera
    turnToAngle(0, -17, 87, 2.5)                        # rotazione verso miniera

    motorTopL.run_angle(1000, -430, Stop.BRAKE, True)   # abbassamento cremagliera
    moveToLight(14, 40, 90, 2.5, False)                 # avanzamento con riferimento a linea (nera)
    moveTime(1200, 80, 90, 2.5)                         # ingroppamento miniera -> sollevamento carrello
    wait(300)

    motorTopL.run_angle(1000, 170, Stop.BRAKE, False)   # ?
    moveToDistance(10, -40, 88, 2.5)                    # arretramento -> uscita da miniera
    motorTopL.run_angle(1000, 250, Stop.BRAKE, True)    # sollevamento cremagliera
    turnToAngle(-20, 0, 65, 2.5)                        # rotazione
    moveToDistance(7, -40, 65, 2.5)                     # allontanamento da miniera con evitamento bordo

    turnToAngle(-20, 0, 0, 2.5)                         # rotazione dritto
    moveToDistance(11, -50, 0, 2.5)                     # posizonamento per scarico sabbia
    motorTopR.run_angle(1000, -700)                     # scarico sabbia (cremagliera?)
    moveToDistance(68, -90, 0, 2.5)                     # ritorno in base

    print("M5 - Tempo impiegato: ", float(stopwatch.time())/1000, " secondi")

# M5()
#tempo = 20sec   