# CARRUCOLA (M11) + M10
from func import *

def M2 ():

    stopwatch = StopWatch()
    clockTime = 1000

    calibImu(1)
    resetImu()
    motorTopL.reset_angle() 

    motorTopL.run_target(1000, 300, Stop.BRAKE, False)

    moveToDistance(63, 50, 0, 2.5)
    turnToAngle(0, 40, -45, 2.5)
    moveToDistance(19, 50, -45, 2.5)
    turnToAngle(0, 30, -90, 2.5)
    moveToDistance(8, 40, -90, 2.5)
    motorMoveL.dc(50)
    wait(1000)
    stopMotorPair()

    motorTopR.run_angle(1000, -1000)

    moveToDistance(40, -50, -90, 2.5)

    print(float(stopwatch.time())/1000, " secondi")

M2 ()
# 16 s