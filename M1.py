# RACCOLTA PESCI E OGGETTI VARI PER IL CAMPO + BOA, PESO MORTO E PINO IL SOMMOZZATORE
from func import *

def M1 ():

    stopwatch = StopWatch()
    clockTime = 1000

    #motorTopR.run_angle(1000, 1200, Stop.HOLD, False) 
    
    resetImu()
    motorTopL.reset_angle()
    motorTopR.reset_angle()

    print(hub.battery.voltage())

    moveToDistance(46, 50, 0, 2.5)                      # avanzamento fino a montagna

    for i in range(3):                                  # batte forte 3 volte
            motorTopL.run_target(1000, -400)
            motorTopL.run_target(1000, 150)
    wait(200)


    moveToDistance(27, 55, 0, 2.5)                      # avanzamento


    turnToAngle(0, 20, -90, 2.5)                        # rotazione -> missione macigni

    turnToAngle(20, 0, -65, 2.5)                        # girazione verso 
    motorTopR.run_angle(1000,-500)

    moveToDistance(13, -40, -65, 2.5)
    turnToAngle(-20, 0, -80, 2.5)

    moveToDistance(16, -45, -100, 2.5)                  #avvicinamento coso rotondo
    
    motorTopR.run_angle(1000, -180)                     #movimento braccio forcato

    moveToDistance(13, -80, -100, 2.5)                  #aggancio coso rotondo

    motorTopR.run_angle(400, 400)                      #alzo il braccio

    moveToDistance(5, 60, -90, 2.5) 



    print("M1 - Tempo impiegato: ", float(stopwatch.time())/1000, " secondi")

M1 ()
# 19.2 sec