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
    for i in range(3):
        motorTopL.run_angle(1000, -150)  #fa uscire i tre smonchi cosi
        motorTopL.run_angle(1000, 200)
        wait(200)
    
    moveToDistance(3, 50, 0 ,2.5, False)
    motorTopL.run_angle(1000, -50)
    moveToDistance(13, 50, 0, 2.5)
    turnToAngle
    

    
    
    # motorTopR.run_target(1000, 400, Stop.HOLD, False)
    # moveToDistance(12, 40, 0, 2.5)

    # motorTopR.run_angle(1000, 3000)



    print(float(stopwatch.time())/1000, " secondi")

M1()