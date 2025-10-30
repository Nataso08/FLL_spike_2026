# Miniera
from func import *

def M5 ():
    stopwatch = StopWatch()
    clockTime = 1000

    resetImu()
    calibImu(2)

    motorTopL.run_angle(1000, 650, Stop.BRAKE, False) #alzo il braccio
    moveToDistance(73, 60, 0, 2.5, False) 
    moveToDistance(12, 35, 0, 2.5) 
    turnToAngle(19, 0, 65, 2.5)
    moveToDistance(14, 40, 65, 2.5) 
    turnToAngle(0, -17, 87, 2.5) #allineato con miniera

    motorTopL.run_angle(1000, -430, Stop.BRAKE, True) #abbasso braccio
    moveToLight(14, 40, 90, 2.5, False)
    moveTime(1200, 80, 90, 2.5)
    wait(300)

    motorTopL.run_angle(1000, 170, Stop.BRAKE, False)#"ingroppata"
    moveToDistance(10, -40, 88, 2.5)
    motorTopL.run_angle(1000, 250, Stop.BRAKE, True)
    turnToAngle(-20, 0, 65, 2.5)
    moveToDistance(7, -40, 65, 2.5)

    turnToAngle(-20, 0, 0, 2.5)
    moveToDistance(11, -50, 0, 2.5)
    motorTopR.run_angle(1000, -700)
    moveToDistance(68, -90, 0, 2.5)

    print(float(stopwatch.time())/1000, " secondi")


M5()
#tempo = 20sec   