import random   # le module random permet la génération aléatoire de nombre
prix = random.randint(1,10)  

score = 200

tentatives = 0

print("Devinez le juste prix qui est un nombre compris entre 1 et 10 inclus.")

while True:
    nombre = int(input())
    tentatives += 1
    if nombre < prix:
        print("Le juste prix est plus haut")
    if nombre > prix:
        print("Le juste prix est plus bas")
    if nombre == prix:
        print("Bravo, vous avez trouvé le juste prix {} en {} essais, votres score est {}.".format(prix, tentatives, int(score/tentatives)))
        print("Partie terminée !!")
        break
    print("Essayez encore !!")

