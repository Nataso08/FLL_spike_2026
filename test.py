# FILE A SCOPO DI TEST DELLE MISSIONI O SINGOLE PARTI
from pybricks.hubs import PrimeHub
from M1 import M1
from M2 import M2
from M3 import M3
from M3_Barca import M3_Barca
from M4 import M4
from M5 import M5
from M6 import M6
from func import *

hub = PrimeHub()

# print("Batteria: ", hub.battery.voltage() / 1000, " V")      # comando per ottenere tensione della batteria (ottimale sopra 8 V)


# se si vuole svolgere una precisa missione utilizzare la seguente sintassi,
# togliendo il nome della missione dal commento e verificare corretta identazione (no spazio a sx)

# M2()

moveToDistanceUltrasound(200, -30, 0, 2.5)
