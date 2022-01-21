'''
3.2 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! 
A program tartalmazza a függvény hívását is!

Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában, és ezt értékelje ki a függvény! 
Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!
'''

def harommal_oszthato(*nums):
    lista = []
    while True:
        beker = int(input('Adj meg számot: \t'))
        if beker < 0:
            break
        elif beker % 3 == 0:
            lista.append(beker)
    return f'3-al osztható számok összege:  {sum(lista)}, száma: {len(lista)}'


print(harommal_oszthato())