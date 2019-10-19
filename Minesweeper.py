import random as rd
import re
from Mine_ui_check import *

def mine_sweeper(größe):
    # Check Liste
    cl = []
    # Leben
    leben = 2
    # Vergleich Feld generieren
    field = [["O" for i in range(größe)] for i in range(größe)]
    # Bomben erschaffen
    if größe <= 3:
        # Bei Feldern die kleiner sind als 3x3 auch eine Bombe erschaffen
        bomben = [[rd.randint(0,größe-1), rd.randint(0,größe-1)]]
    else:
        # 20% des Feldes sind Bomben
        bomben = [[rd.randint(0,größe-1), rd.randint(0,größe-1)] for x in range(round((20*(größe*größe))//100))]
    # Dev zeug
    #print(bomben)
    #print("Generated:", len(bomben), "bombs")
    #print(rn)
    print()
    # Bomben ins Feld bringen
    for i in bomben:
        b_höhe, b_breite = i
        if field[b_höhe][b_breite] == "O":
            field[b_höhe][b_breite] = "+"
        else:
            # Dev Zeug
            #print("Duplicate")
            # Bomben können nicht an der selben stelle spawnen
            while True:
                b_höhe = rd.randint(0,größe-1)
                b_breite =rd.randint(0,größe-1)
                if field[b_höhe][b_breite] == "+":
                    continue
                else:
                    field[b_höhe][b_breite] = "+"
                    break

    for z in range(len(field)):
        for s in range(len(field[z])):
            zr = range(z-1, z+2)
            sr = range(s-1, s+2)
            if field[z][s] != "+":

                for i in zr:
                        for j in sr:
                            try:
                                if j >= 0 and i >= 0:
                                    cl.append(field[i][j])
                                else:
                                    pass

                            except IndexError:
                                pass

                ndb = cl.count("+")
                field[z][s] = str(ndb)
                cl = []

            else:
                pass

    for z in field:
        print(z)

    print()

    # Feld welches der User sieht und spielt
    ufield = [["O" for i in range(größe)] for i in range(größe)]
    for uf in ufield:
        print(uf)

    print()

    # User gibt Feld ein und es wird geprüft
    inputcheck(field, ufield, größe)
    # Schaut ob man gewonnen oder verloren hat

# Input für die Größe des Feldes
while True:
    try:
        g = int(input("Welche größe?: "))
        if g <= 0:
            raise
        break
    except:
        print("Bitte nur ganze Zahlen eingeben")
        continue

# Main funktion
mine_sweeper(g)
