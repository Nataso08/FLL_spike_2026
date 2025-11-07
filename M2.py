# CARRUCOLA (M11) + M10
from func import *

def M2 ():
    stopwatch = StopWatch()
    clockTime = 1000

    calibImu(1)
    resetImu()
    motorTopL.reset_angle()

    # tira su braccio
    motorTopL.run_target(1000, 300, Stop.BRAKE, False)

    # avanti fino a carrucola e indietro per reimpostare il braccio elastico
    moveToDistance(90, 60, 0, 2.5)
    moveToDistance(9, -40, 0, 2.5)

    # carrucola
    turnToAngle(0, 30, -90, 2.5)
    moveToDistance(12, 40, -100, 2.5, False)
    moveToDistance(9, 80, -115, 2.5)
    motorTopR.run_angle(1000, -1000)
    
    # da carrucola ad anello
    moveToDistance(41, -60, -90, 2.5)

    # allineamento anello
    moveToDistance(9, 50, -90, 2.5)

    # tira anel
    motorTopL.run_target(1000, -120)
    motorTopL.run(-100)
    moveToDistance(2, 25, -90, 2.5)
    motorTopL.brake()
    turnToAngle(35, 0, 0, 2.5)
    moveToDistance(60, 80, 0, 2.5, False)
    moveToDistance(45, 100, -30, 2.5)
    moveToDistance()

    print("M2 - Tempo impiegato: ", float(stopwatch.time())/1000, " secondi")

M2 ()
#tempo = 19sec