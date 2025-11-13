# FILE A SCOPO DI TEST DELLE MISSIONI O SINGOLE PARTI
from pybricks.hubs import PrimeHub
# from M1 import M1
from func import *

hub = PrimeHub()

print("Batteria: ", hub.battery.voltage() / 1000, " V")      # comando per ottenere tensione della batteria (ottimale sopra 8 V)

# se si vuole svolgere una precisa missione utilizzare la seguente sintassi,
# M1 ()
# togliendo il nome della missione dal commento e verificare corretta identazione (no spazio a sx)

#Struttura m1 campo 2024/2025 che si muove - utile per open day 2025
motorTopL.run_angle(3000, -400)
wait(100)
motorTopR.run_angle(1000, -800)
wait(1300)
motorTopR.run_angle(1000, 800)
wait(100)
motorTopL.run_angle(3000, 400)
wait(100)

#motorTopR.run_angle(1000, -7000)


# RACCOLTA PESCI E OGGETTI VARI PER IL CAMPO + BOA, PESO MORTO E PINO IL SOMMOZZATORE
