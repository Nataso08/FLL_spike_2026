# CARRUCOLA (M11) + M10
from func import *

def M2 ():

    stopwatch = StopWatch()
    clockTime = 1000

    calibImu(2)
    resetImu()

    moveToDistance(15, 40, 0, 2.5)
    turnToAngle(0, 25, -90, 2.5)
    moveToDistance(43, 40, -90, 2.5)
    turnToAngle(0, 25, -180, 2.5)
    moveToDistance(8, 30, -180, 2.5)
    motorMoveL.dc(50)
    wait(500)
    stopMotorPair()

    waitPress()
    motorTopR.run_target(1000, -1500)
    wait(1000)
    moveToDistance(8, -25, -180, 2.5)


    # print(float(stopwatch.time())/1000, " secondi")
