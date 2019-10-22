import random as rd
import re
from Mine_ui_check import *

def mine_sweeper(größe):
    # Check List
    cl = []
    # Lives
    leben = 2
    # Generating check field
    field = [["O" for i in range(größe)] for i in range(größe)]
    # Creating bombs
    if größe <= 3:
        # Fields smaller than 3x3 should have bombs too
        bomben = [[rd.randint(0,größe-1), rd.randint(0,größe-1)]]
    else:
        # 20% of the field are bombs
        bomben = [[rd.randint(0,größe-1), rd.randint(0,größe-1)] for x in range(round((20*(größe*größe))//100))]
    # Dev zeug
    #print(bomben)
    #print("Generated:", len(bomben), "bombs")
    #print(rn)
    print()
    # Bringing bombs into field
    for i in bomben:
        b_höhe, b_breite = i
        if field[b_höhe][b_breite] == "O":
            field[b_höhe][b_breite] = "+"
        else:
            # Dev Zeug
            #print("Duplicate")
            # Bombs cannot spawn in same place
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

    # User field
    ufield = [["O" for i in range(größe)] for i in range(größe)]
    for uf in ufield:
        print(uf)

    print()

    # Inputcheck function
    inputcheck(field, ufield, größe)

# Field size
while True:
    try:
        g = int(input("Which size: "))
        if g <= 0:
            raise
        break
    except:
        print("Only positive integers!")
        print("Don't cheat")
        continue

# Main function
mine_sweeper(g)
