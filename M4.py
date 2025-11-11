# nave
from func import *

def M4 ():

    stopwatch = StopWatch()
    clockTime = 1000
    
    resetImu()

    moveToDistance(30, 60, 0, 2.5, False)       # avanzamento
    moveToDistance(9, 40, 0, 2.5)               # avanzamento lento fino a missione

    moveToDistance(6, -70, 0, 2.5)              # arretramento -> rimozione sabbia

    moveTime(1200, 80, 10, 2.5)                 # ingroppamento missione -> sollevamento barca + deposito sabbia

    moveToDistance(50, -80, 5, 2.5)             # ritorno in base

    print("M4 - Tempo impiegato: ", float(stopwatch.time())/1000, " secondi")

# M4 ()
#tempo = 6sec