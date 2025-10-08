from func import *

def M3 ():
    
    stopwatch = StopWatch()
    clockTime = 1000

    moveToDistance(60, 50, 0, 2.5, False)
    moveToDistance(6, 30, 0, 2.5)
    wait(100)
    turnToAngle(0, 20, -45, 2.5)
    moveToDistance(10, 40, -45, 2.5, False)
    moveToDistance(15, 80, -45, 2.5)
    moveToDistance(3, -40, -45, 2.5)
    moveToDistance(5, 90, -45, 2.5)
    wait(300)
    moveToDistance(20, -50, -45, 2.5)

    turnToAngle(20, -20, 0, 2.5)
    moveToDistance(60, -50, 0, 2.5, False)


    print(float(stopwatch.time())/1000, " secondi")