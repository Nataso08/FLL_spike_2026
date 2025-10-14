# nave
from func import *

def M4 ():

    stopwatch = StopWatch()
    clockTime = 1000
    
    resetImu()
    # calibImu(2)

    moveToDistance(30, 60, 0, 2.5, False)
    moveToDistance(9, 40, 0, 2.5)
    moveToDistance(5, -40, 0, 2.5)
    moveTime(1000, 90, 5, 2.5)
    # moveToDistance(200, -40, 5, 2.5)
    # moveToDistance(200, 40, 5, 2.5)
    moveToDistance(60, -80, 5, 2.5)




    print(float(stopwatch.time())/1000, " secondi")

M4 ()
#tempo = 6sec