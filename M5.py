# Miniera
from func import *

def M5 ():
    stopwatch = StopWatch()
    clockTime = 1000
    
    resetImu()
    calibImu(2)

    motorTopL.run_target(1000, -1450, Stop.BRAKE, False) #alzo il braccio

    moveToDistance(73, 60, 0, 2.5, False) 
    moveToDistance(12, 35, 0, 2.5) 
    turnToAngle(19, 0, 60, 2.5)
    moveToDistance(10, 40, 65, 2.5) 
    turnToAngle(0, -17, 87, 2.5) #allineato con miniera

    motorTopL.run_target(1000, -250, Stop.BRAKE, True) #abbasso braccio
    moveToDistance(5, 40, 90, 2.5)
    moveToDistance(15, 45, 90, 2.5)#arrivo dentro miniera
    waitPress()

    motorTopL.run_target(1000, -850, Stop.BRAKE,True)#"ingroppata"
    moveToDistance(13, -40, 90, 2.5)
    motorTopL.run_target(700, 300, Stop.BRAKE, False)
    turnToAngle(5, 19, 30, 2.5)
    moveToDistance(87, -60, 30, 2.5) 

    #print(float(stopwatch.time())/1000, " secondi")


M5()
#tempo =    