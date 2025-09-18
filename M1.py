# RACCOLTA PESCI E OGGETTI VARI PER IL CAMPO + BOA, PESO MORTO E PINO IL SOMMOZZATORE
from func import *

from pybricks.tools import StopWatch

def M1 ():

    stopwatch = StopWatch()
    clockTime = 1000

    # cremagliera orizzontale: valori positivi = sinistra
    # corsa cremagliera: 1650 gradi

    # global time_run
    
    k=-5                                 # parametro per correggere rettilineo palombaro (andare a sx k<0, dx k>0)
    
    resetImu()                                              # reset giroscopio
    calibImu(2)                                             # reset giroscopio

    # time_run = StopWatch.time()

    motorTopR.run_angle(-500, 300, Stop.BRAKE, False)       # spostamento cremagliera verso destra
    moveToDistance(60, 50, 0, 2.5, False)                   # primo rettilineo
    motorTopR.run_angle(1000, 300, Stop.BRAKE, False)       # inizio spostamento cremagliera a sinistra
    moveToDistance(11, 45, 0, 2.5)                          # avanzamento
    motorTopR.run_angle(800, 100)                           # spostamento cremagliera e raccolta boa
    
    turnToAngle(0, 30, -86, 1.3)                            # rotazione robot verso zona nord
    motorTopR.run_angle(-800, 200, Stop.BRAKE, False)       # spostamento creamgliera per evitare sonar
    
    moveToDistance(30, 45, -87, 2.5, False)                 # avanzamento robot verso peso morto
    motorTopR.run_angle(-800, 200, Stop.BRAKE, False)       # posizionamento verso pesce
    moveToDistance(46, 45, -87, 2.5)                        # avanzamento robot

    motorTopR.run_angle (1000, 1600)                        # spostamento cremagliera e raccolta peso morto
    moveToDistance(5, 45, -90, 2.5, False)                  # avanzamento

    motorTopR.run_angle(-1000, 1650, Stop.BRAKE, False)     # raccolta peso morto in parallelo con avanzamento
    moveToDistance(19, 45, -90, 2.5)                        # avanzamento fino ai fiori
    motorTopL.run_angle(500, 340, Stop.BRAKE, False)        # pre-abbassamento braccio palombaro
    moveToDistance(33, 45, -90+k, 2.5)                      # avanzamento verso area finale

    motorTopR.run_angle(800, 800)                           # spostamento cremagliera verso destra (coral buds e squalo)
    moveToDistance(7, 40, -90, 2.5)                         # avanzamento
    moveTime (1000, 30, -90, 2.5)                           # avanzamento e pressione coral buds

    motorTopL.run_angle(-600, 120)                          # sollevamento Pino il Sommozzatore
    moveToDistance(3, -30, -90, 2.5)                        # arretramento
    motorTopL.run_angle(-500, 160, Stop.BRAKE, False)       # sollevamento braccio palombaro
    motorTopR.run_angle(800, 250, Stop.BRAKE, False)        # spostamento cremagliera a destra in parallelo
    motorTopR.run_angle(-1000, 1200, Stop.BRAKE, False)
    turnToAngle (-30, 10, -140, 1.3)                        # rotazione parziale verso base 2
    motorTopR.run_angle(-1000, 100, Stop.BRAKE, False)
    turnToAngle (0, 40, -180, 1.3)                          # rotazione finale verso base 2 (2 rotazioni impediscono blocco robot)

    moveToDistance(37, 80, -180, 2.5)                       # avanzamento verso base e raccolta coralli finali
    turnToAngle (80, 62, -120, 1.3)                         # rotazione verso base
    moveToDistance(5, 80, -120, 2.5)


    # print(float(stopwatch.time())/1000, " secondi")