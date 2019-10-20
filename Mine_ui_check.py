import re

def inputcheck(cfield, ufield, feldg):

    rn = int(round((30*(feldg**2))//100))
    print("You have to get", rn, "fields right to win!")
    print()

    cl = []
    leben = 2
    richtig = 0

    while leben != 0 and richtig != rn:
        while True:
            ui = input("Which field (Row, Column): ")
            print()
            # Finds all numbers
            fin = re.findall("[0-9]+",ui)
            #print(fin)
            if len(fin) > 2 or len(fin) == 1 or len(fin) == 0:
                print("Please use the foramt given")
                print()
                continue
            else:
                break

        # Working with the coordinates
        ui_höhe, ui_breite = fin
        ui_höhe = int(ui_höhe)-1
        ui_breite = int(ui_breite)-1

        # Checking if field is a bomb or not
        try:
            if cfield[ui_höhe][ui_breite] == "+":
                print("Bomb")
                print()
                leben -= 1
                ufield[ui_höhe][ui_breite] = "+"
                if leben != 0:
                    for i in ufield:
                        print(i)
                print()
            else:
                print("No bomb")
                ufield[ui_höhe][ui_breite] = cfield[ui_höhe][ui_breite]

                for i in ufield:
                    print(i)

                richtig += 1
        # If coordinates are not in the field
        except IndexError:
            print("Please input coordinates in the field")
            continue

    if richtig == rn:
        print("You win!")
    else:
        print("You lost. The field was:")

        for i in cfield:
            print(i)
#inputcheck()
