# RACCOLTA PESCI E OGGETTI VARI PER IL CAMPO + BOA, PESO MORTO E PINO IL SOMMOZZATORE
from func import *

def M1 ():

    stopwatch = StopWatch()
    clockTime = 1000

    #motorTopR.run_angle(1000, 1200, Stop.HOLD, False) 
    
    resetImu()
    # calibImu(2)

    print(hub.battery.voltage())

    moveToDistance(46, 50, 0, 2.5)

    for i in range(4):
            motorTopL.run_target(1000, -400)
            motorTopL.run_target(1000, 150)
    wait(200)
    

    moveToDistance(28, 50, 0, 2.5)

    turnToAngle(0, 25, -80, 2.5)

    moveToDistance(11, 40, -80, 2.5)

    wait(100)
    moveToDistance(18, -40, -55, 2.5)

    motorTopR.run_angle(-400, 700, Stop.HOLD, False)
    
    turnToAngle(-25, 0, -100, 2.5)
    moveToDistance(26, -40, -100, 2.5)

    motorTopR.run_angle(-400, -200)

    waitPress()

    moveToDistance(4, -40, -90, 2.5)
    turnToAngle(8, -30, -5, 2.5)


    print(float(stopwatch.time())/1000, " secondi")

M1()