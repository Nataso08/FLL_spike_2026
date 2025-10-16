# FAVRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRERRRRRRRRRRRRRRETT
from  func import *

def M3 ():

    stopwatch = StopWatch()
    clockTime = 1000
    print(hub.battery.voltage(), " mV")

    motorTopL.reset_angle()
    resetImu()

    motorTopR.run_target(1000, 1100, Stop.HOLD, False)

    moveToDistance(68, 70, 0, 2.5)
    moveToDistance(19, -70, 0, 2.5)
    moveToDistance(9, 40, 0, 2.5)

    motorTopL.run_angle(1000, -1000)
    wait(200)
    motorTopL.run_angle(1000, 1000)

    turnToAngle(20, 0, 35, 2.5)

    moveToDistance(11, 40, 35, 2.5)
    turnToAngle(0, 20, -45, 2.5)
    motorTopR.run_target(1000, 300)
    moveToDistance(10, 40, -45, 2.5)
    motorTopR.run_target(1000, 1200)
    
    moveToDistance(10, -60, -45, 2.5)
    turnToAngle(0, -30, 20, 2.5)
    moveToDistance(80, -80, 20, 2.5) 

    print(float(stopwatch.time())/1000, " secondi")

    

M3 ()
#tempo = 18sec