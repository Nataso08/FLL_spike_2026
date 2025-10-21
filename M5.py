# Miniera
from func import *

def M5 ():
    stopwatch = StopWatch()
    clockTime = 1000
    
    resetImu()
    calibImu(2)

    motorTopL.run_target(1000, 580, Stop.BRAKE, False) #alzo il braccio

    moveToDistance(73, 60, 0, 2.5, False) 
    moveToDistance(12, 35, 0, 2.5) 
    turnToAngle(19, 0, 65, 2.5)
    moveToDistance(14, 40, 65, 2.5) 
    turnToAngle(0, -17, 87, 2.5) #allineato con miniera

    motorTopL.run_target(1000, 150, Stop.BRAKE, True) #abbasso braccio
    # moveToDistance(5, 40, 90, 2.5)
    # moveToDistance(13, 45, 90, 2.5, False)#arrivo dentro miniera
    moveToLight(14, 40, 90, 2.5, False)
    moveTime(1200, 45, 90, 2.5)
    wait(300)

    motorTopL.run_target(1000, 450, Stop.BRAKE, True)#"ingroppata"
    moveToDistance(12, -40, 90, 2.5)
    motorTopL.run_target(1000, 580, Stop.BRAKE, True)
    turnToAngle(-25, 0, 25, 2.5)
    moveToDistance(12, -40, 25, 2.5)
    turnToAngle(-20, 0, 0, 2.5)
    moveToDistance(2, -50, 0, 2.5)


    #print(float(stopwatch.time())/1000, " secondi")


M5()
#tempo =    