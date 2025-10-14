from func import *

def M5 ():
    stopwatch = StopWatch()
    clockTime = 1000
    
    resetImu()
    calibImu(2)

    motorTopL.reset_angle() 
    motorTopL.run_angle(1000, 300, Stop.BRAKE, False) #alzo il braccio

    moveToDistance(86, 40, 0, 2.5) 
    turnToAngle(20, 0, 60, 2.5)
    moveToDistance(9, 40, 60, 2.5) 
    turnToAngle(0, -20, 85, 2.5) #allineato con miniera

    waitPress()

    moveToDistance(5, 40, 90, 2.5)
    motorTopL.run_target(1000, -150, Stop.BRAKE, True) #abbasso braccio
    moveToDistance(11, 50, 90, 2.5)
M5()
#tempo =    