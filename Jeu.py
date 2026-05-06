import random
for i in range(3):
    choix = ["pierre", "feuille", "ciseaux"]

    j = input("pierre / feuille / ciseaux : ")
    o = random.choice(choix)

    print("ordi :", o)

    if j == o:
        print("égalité")
    elif (j == "pierre" and o == "ciseaux") or (j == "papier" and o == "pierre") or (j == "ciseaux" and o == "papier"):
        print("gagné")
    else:
        print("perdu")
