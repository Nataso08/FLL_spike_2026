# RACCOLTA PESCI E OGGETTI VARI PER IL CAMPO + BOA, PESO MORTO E PINO IL SOMMOZZATORE
from func import *

def M1 ():

    stopwatch = StopWatch()
    clockTime = 1000

    #motorTopR.run_angle(1000, 1200, Stop.HOLD, False) 
    
    resetImu()
    # calibImu(2)

    print(hub.battery.voltage())

    moveToDistance(55, 50, 0, 2.5, False)
    motorTopR.run_target(1000, 400, Stop.HOLD, False)
    moveToDistance(12, 40, 0, 2.5)

    motorTopR.run_angle(1000, 3000)



    print(float(stopwatch.time())/1000, " secondi")

M1()