# RACCOLTA PESCI E OGGETTI VARI PER IL CAMPO + BOA, PESO MORTO E PINO IL SOMMOZZATORE
from func import *

def M1 ():

    stopwatch = StopWatch()
    clockTime = 1000
    
    resetImu()
    # calibImu(2)

    print(hub.battery.voltage())

    moveToDistance(35, 50, 0, 2.5, False)
    motorTopR.run_target(1000, 400, Stop.HOLD, False)
    moveToDistance(17, 40, 0, 2.5)

    for _ in range(4):
        motorTopR.run_target(800, 400)
        wait(200)
        motorTopR.run_target(1000, 0)
        wait(200)



    print(float(stopwatch.time())/1000, " secondi")