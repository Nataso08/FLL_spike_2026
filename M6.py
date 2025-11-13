from func import *

def M6 ():
    stopwatch = StopWatch()
    clockTime = 1000

    calibImu(1)
    resetImu()

    moveToDistance(2,30,20,2.5) #Partenza
    turnToAngle(20,0,42,2.5)
    moveToDistance(43,40,52,2.5) #Arrivo in piazzetta
    waitPress()
    wait(100)
    moveToDistance(20,-40,52,2.5) #Retro
    motorTopL.run_angle(500,-300) #Lascio il contenitore
    waitPress() #Punto dove abbiamo perfeionato - giorno 13-11-2025
    moveToDistance(60,40,90,2.5)  #Rettilineo verso spazietto 
    moveToDistance(60,30,34,2.5)
    moveToDistance(8,20,0,2.5)
    wait(200)
    moveToDistance(27,-40,-41,2.5) #Alza ostacolo nella sezione M1 



    #motorTopL.run_target(1000, -700)







    print("M6 - Tempo impiegato: ", float(stopwatch.time())/1000, " secondi")
    

M6()