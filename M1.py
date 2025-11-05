# RACCOLTA PESCI E OGGETTI VARI PER IL CAMPO + BOA, PESO MORTO E PINO IL SOMMOZZATORE
from func import *

def M1 ():

    stopwatch = StopWatch()
    clockTime = 1000

    #motorTopR.run_angle(600, 1200, Stop.HOLD, False) 
    
    
    resetImu()
    calibImu(2)

    print(hub.battery.voltage())

    moveToDistance(45, 50, 0, 2.5)
    #motorTopL.run_target(1500, -400) #Colpi energetici,violenti
    #motorTopL.run_target(1000, 200)

    #motorTopL.run_target(1500, -400)
    #motorTopL.run_target(1000, 200)

    #motorTopL.run_target(1500, -400)
    #motorTopL.run_target(1000, 200)

    #motorTopL.run_target(1500, -400)
    #motorTopL.run_target(1000, 200)


    moveToDistance(30, 40, 0, 2.5)

    turnToAngle(0,13,-33,2.5)
    
 

    moveToDistance(-10,10,0,2.5)
    
    #motorTopL.run_target(500, -100)
    #motorTopR.run_angle(700, -700)
    #motorTopR.run_angle(600, 600)

    print("M1 - Tempo impiegato: ")
    print(float(stopwatch.time())/1000, " secondi")

M1()