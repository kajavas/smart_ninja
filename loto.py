#def lotto(obmocje, st_stevilk):
    #obmocje: 1 --> 39
    #st_stevilk: koliko stevil izberem
    #vrne naj nakljucno izbrana stevila
    #vrne naj listo izbranih stevilk

import random

def lotto(obmocje, stevilo_stevilk):
    lista_izbranih_stevilk = []

    for zreb in range(stevilo_stevilk):
        stevilka = random.choice(obmocje)
        lista_izbranih_stevilk.append(stevilka)
        obmocje.remove(stevilka)

    return lista_izbranih_stevilk

obmocje_stevil = list(range(1, 40))

lotto_kombinacija = lotto(obmocje_stevil, 7)

print(lotto_kombinacija)