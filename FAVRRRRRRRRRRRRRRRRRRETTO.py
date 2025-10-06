from  func import *

def FAVRRRETTO ():

    stopwatch = StopWatch()
    clockTime = 1000

    motorTopL.reset_angle()
    resetImu()



    moveToDistance(68, 70, 0, 2.5)
    moveToDistance(19, -50, 0, 2.5)
    moveToDistance(9, 40, 0, 2.5)

    motorTopL.run_angle(1000, -600)
    wait(200)
    motorTopL.run_angle(1000, 600)

    turnToAngle(20, 0, 30, 2.5)
    moveToDistance(17, 40, 30, 2.5)

    turnToAngle(0, 20, -45, 2.5)

    motorTopR.run_angle(1000, 200)

    moveToDistance(10, 40, -45, 2.5)

    motorTopR.run_angle(1000, -200)

    moveToDistance(20, -50, -45, 2.5)

    turnToAngle(0, -30, 20, 2.5)

    moveToDistance(80, -80, 20, 2.5)

    print(float(stopwatch.time())/1000, " secondi")

    

FAVRRRETTO ()