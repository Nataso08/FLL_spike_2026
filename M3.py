# FAVRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRERRRRRRRRRRRRRRETTOO
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

    motorTopL.run_angle(1000, -1100) #abbocca il "tridente"
    wait(250)
    motorTopL.run_angle(1000, 1000)

    turnToAngle(20, 0, 35, 2.5)

    moveToDistance(10, 40, 35, 2.5)
    turnToAngle(0, 15, -45, 2.5)

    #waitPress();
    motorTopR.run_target(1100, 340) #svolge missione "parco degli spacciatori"
    moveToDistance(9, 35, -40, 2.5)
    motorTopR.run_target(1000, 1200)
    
    moveToDistance(10, -60, -45, 2.5)
    turnToAngle(0, -20, 29, 2.5)
    moveToDistance(75, -78, 20, 2.5) 
   
    print("M3 - Tempo impiegato: ")
    print(float(stopwatch.time())/1000, " secondi")
  

M3 ()
#tempo = 18sec