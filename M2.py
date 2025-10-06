# CARRUCOLA (M11) + M10
from func import *

def M2 ():

    stopwatch = StopWatch()
    clockTime = 1000

    calibImu(1)
    resetImu()
    motorTopL.reset_angle()

    motorTopL.run_target(1000, 300, Stop.BRAKE, False)

    moveToDistance(72, 50, 0, 2.5, False)
    moveToDistance(4, 35, 0, 2.5)
    turnToAngle(0, 25, -90, 2.5)
    moveToDistance(13, 40, -90, 2.5, False)
    moveToDistance(10, 80, -110, 2.5)

    motorTopR.run_angle(1000, -1000)

    moveToDistance(41, -60, -90, 2.5)

    moveToDistance(8, 50, -90, 2.5)

    motorTopL.run_target(1000, -50)
    motorTopL.run(-300)
    moveToDistance(2, 35, -90, 2.5)
    motorTopL.brake()
    turnToAngle(35, 0, 0, 2.5)
    moveToDistance(60, 90, 0, 2.5, False)
    moveToDistance(45, 80, -30, 2.5)



    print(float(stopwatch.time())/1000, " secondi")

M2 ()