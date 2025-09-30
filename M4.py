# nave
from func import *

def M4 ():

    stopwatch = StopWatch()
    clockTime = 1000
    
    resetImu()
    # calibImu(2)

    moveToDistance(32, 60, 0, 2.5, False)
    moveToDistance(9, 40, 0, 2.5)
    moveToDistance(5, -40, 0, 2.5)
    moveToDistance(14, 70, 5, 2.5)
    moveToDistance(50, -60, 5, 2.5)




    print(float(stopwatch.time())/1000, " secondi")

M4()