# RACCOLTA PESCI E OGGETTI VARI PER IL CAMPO + BOA, PESO MORTO E PINO IL SOMMOZZATORE
from func import *

def M1 ():

    stopwatch = StopWatch()
    clockTime = 1000

    #motorTopR.run_angle(1000, 1200, Stop.HOLD, False) 
    
    resetImu()

    print(hub.battery.voltage())

    moveToDistance(46, 50, 0, 2.5)                      # avanzamento fino a montagna

    for i in range(3):                                  # batte forte 4 volte
            motorTopL.run_target(1000, -400)
            motorTopL.run_target(1000, 150)
    wait(200)


    moveToDistance(28, 55, 0, 2.5)                      # avanzamento


    turnToAngle(0, 20, -90, 2.5)                        # rotazione -> missione macigni

    #moveToDistance(10, 40, -80, 2.5)                    # avanzamento -> missione piatto


    turnToAngle(20,0,-65,2.5)
    motorTopR.run_angle(-800, 300)
    moveToDistance(15,-40,-65,2.5)
    turnToAngle(-20,0,-80,2.5)

    moveToDistance(16,-45,-100,2.5)
    motorTopR.run_angle(-400, 380)
    moveToDistance(13,-45,-100,2.5)
    moveToDistance(5,45,-90,2.5)





    #wait(100)
    #moveToDistance(18, -40, -55, 2.5)                   # arretramento

    #waitPress()
    # motorTopR.run_angle(-400, 700, Stop.HOLD, False)    # abbassamento braccio per raccolta peso
    
    # waitPress()
    # turnToAngle(-25, 0, -100, 2.5)                      # allineamento
    # waitPress()
    # moveToDistance(26, -40, -100, 2.5)                  # arretramento

    # waitPress()
    # motorTopR.run_angle(-400, -200)                     # sollevamento braccio per raccolta peso

    # waitPress()
    # moveToDistance(4, 40, -90, 2.5)                     # avanzamento breve -> si spostano pietre
    # waitPress()
   
   
    # moveToDistance(8, -40, -90, 2.5)                    # arretramento verso base
    # waitPress()
    # turnToAngle(8, -30, -5, 2.5)                        # rotazione -> ingresso in base

    print("M1 - Tempo impiegato: ", float(stopwatch.time())/1000, " secondi")

M1 ()