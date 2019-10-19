import re

def inputcheck(cfield, ufield, feldg):

    rn = int(round((30*(feldg**2))//100))
    print("Es ist/sind", rn, "Feld/er nötig um zu gewinnen")
    print()

    cl = []
    leben = 2
    richtig = 0

    while leben != 0 and richtig != rn:
        while True:
            ui = input("Welches Feld (Zeile, Spalte): ")
            print()
            # Findet alle Zahlen um Koordinaten daraus zu machen
            fin = re.findall("[0-9]+",ui)
            #print(fin)
            if len(fin) > 2 or len(fin) == 1 or len(fin) == 0:
                print("Bitte Format beachten")
                print()
                continue
            else:
                break

        # Aufteilen der Koordinaten in der Liste fin
        ui_höhe, ui_breite = fin
        ui_höhe = int(ui_höhe)-1
        ui_breite = int(ui_breite)-1

        # Testen ob Feld Bombe ist oder nicht
        try:
            if cfield[ui_höhe][ui_breite] == "+":
                print("Bombe")
                print()
                leben -= 1
                ufield[ui_höhe][ui_breite] = "+"
                if leben != 0:
                    for i in ufield:
                        print(i)
                print()
            else:
                print("Keine Bombe")
                # 3x3 Feld um den Punkt wird ausgewählt
                zr = range(ui_höhe-1, ui_höhe+2)
                sr = range(ui_breite-1, ui_breite+2)

                # 3 Zeilen
                for i in zr:
                    # 3 Spalten
                    for j in sr:
                        # Dev zeug um zu schauen ob die Felder stimmen
                        #print("Raw Feld", i, j, "ist", cfield[i][j])
                        try:
                            if j >= 0 and i >= 0:
                                # Dev Zeug
                                #print("Feld", i, j, "ist", cfield[i][j])
                                cl.append(cfield[i][j])
                            else:
                                pass

                        except IndexError:
                            pass

                richtig += 1
                # Dev Zeug
                #print(cl)

                # Zählt die "X" in cl
                ndb = cl.count("+")

                ufield[ui_höhe][ui_breite] = str(ndb)

                cl = []

                for i in ufield:
                    print(i)

        # Wenn spieler Koordinaten über dem Feld angibt
        except IndexError:
            print("Bitte Koordinaten in der Liste angeben")
            continue

    if richtig == rn:
        print("Gewonnen")
    else:
        print("Verloren. Das Feld war:")

        for i in cfield:
            print(i)
#inputcheck()
