# FAVRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRERRRRRRRRRRRRRRETT
from  func import *

def M3 ():

    stopwatch = StopWatch()
    clockTime = 1000
    print(hub.battery.voltage(), " mV")

    motorTopL.reset_angle()
    resetImu()

    motorTopR.run_target(1000, 1200, Stop.HOLD, False) #partenza

    moveToDistance(68, 70, 0, 2.5) #arrivo in missione
    moveToDistance(19, -70, 0, 2.5)
    moveToDistance(8, 40, 0, 2.5)

    motorTopL.run_angle(1000, -1000) #abbocca il "tridente"
    wait(200)
    motorTopL.run_angle(1000, 1000)

    turnToAngle(20, 0, 35, 2.5)

    moveToDistance(11, 40, 35, 2.5)
    turnToAngle(0, 20, -45, 2.5)

    motorTopR.run_target(1100, 330) #svolge missione "parco degli spacciatori"
    moveToDistance(9, 35, -38, 2.5)
    motorTopR.run_target(1000, 1200)
    
    moveToDistance(10, -60, -45, 2.5)
    turnToAngle(0, -23, 29, 2.5)
    moveToDistance(80, -80, 20, 2.5) 

    print(float(stopwatch.time())/1000, " secondi")

    

M3 ()
#tempo = 18sec