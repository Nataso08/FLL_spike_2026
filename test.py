# FILE A SCOPO DI TEST DELLE MISSIONI O SINGOLE PARTI
from pybricks.hubs import PrimeHub
# from M1 import M1
from func import *

hub = PrimeHub()

print("Batteria: ", hub.battery.voltage() / 1000, " V")      # comando per ottenere tensione della batteria (ottimale sopra 8 V)

# se si vuole svolgere una precisa missione utilizzare la seguente sintassi,
# togliendo il nome della missione dal commento e verificare corretta identazione (no spazio a sx)

motorTopL.run_angle(1000, -100)
waitPress()
motorTopL.run_angle(1000, 2000)
#motorTopR.run_angle(1000, -7000)
