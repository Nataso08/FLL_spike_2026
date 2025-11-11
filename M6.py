from func import *

def M6 ():
    stopwatch = StopWatch()

    resetImu()

    motorTopL.run_target(1000, -700)







    print("M6 - Tempo impiegato: ", float(stopwatch.time())/1000, " secondi")
    

M6()