# CARRUCOLA (M11) + M10
from func import *

def M2 ():

    stopwatch = StopWatch()
    clockTime = 1000

    calibImu(2)
    resetImu()

    moveToDistance(77, 40, 0, 2.5)
    turnToAngle(0, 25, -90, 2.5)
    moveToDistance(10, 40, -90, 2.5, False)
    moveToDistance(10, 80, -95, 2.5)

    # turnToAngle(25, 0, -80, 2.5)
    # moveToDistance(5, 80, -90, 2.5)
    # turnToAngle(-30, 0, -95, 2.5)

    motorTopR.run_angle(1000, -2000)

    moveToDistance(40, -40, -90, 2.5)





    # print(float(stopwatch.time())/1000, " secondi")

M2()