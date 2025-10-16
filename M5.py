from func import *

def M5 ():
    stopwatch = StopWatch()
    clockTime = 1000
    
    resetImu()
    calibImu(2)

    motorTopL.reset_angle() 
    motorTopL.run_angle(200, 300, Stop.BRAKE, False) #alzo il braccio

    moveToDistance(73, 60, 0, 2.5, False) 
    moveToDistance(12, 35, 0, 2.5) 
    turnToAngle(19, 0, 60, 2.5)
    moveToDistance(10, 40, 65, 2.5) 
    turnToAngle(0, -19, 87, 2.5) #allineato con miniera


    #motorTopL.run_target(1000, -150, Stop.BRAKE, True) #abbasso braccio
    moveToDistance(5, 40, 90, 2.5)
    moveToDistance(15, 55, 90, 2.5)


    motorTopL.run_angle(1000, 120)
    moveToDistance(13, -40, 90, 2.5)
    motorTopL.run_target(700, 300, Stop.BRAKE, False)
    turnToAngle(5, 19, 30, 2.5)
    moveToDistance(87, -60, 30, 2.5) 




M5()
#tempo =    