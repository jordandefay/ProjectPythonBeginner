import random   # le module random permet la génération aléatoire de nombre
prix = random.randint(1,10)  # génère un nombre aléatoire entre 1 et 10 inclus et le stocke dans la variable 'prix'.

score = 200 # le score maximum que le joueur pourra atteindre en effectuant une seule tentative

tentatives = 0 # initialise le nombre de tentative à 0

print("Devinez le juste prix qui est un nombre compris entre 1 et 10 inclus.") # affiche à l'écran utilisateur

while True: # création d'une "boucle"
    nombre = int(input()) # permet à l'utilisateur de rentrer un nombre au choix
    tentatives += 1
    
    if nombre < prix: # si le nombre entré par l'utilisateur est plus petit que le prix
        print("Le juste prix est plus haut")
        
    elif nombre > prix: # si le nombre entré par l'utilisateur est plus haut que le prix
        print("Le juste prix est plus bas")
        
    else: # si le nombre entré par l'utilisateur est égal au prix
        print("Bravo, vous avez trouvé le juste prix {} en {} essais, votres score est {}.".format(prix, tentatives, int(score/tentatives))) #.format() va permettre d'afficher le juste prix, le nombre de tentative effectué et le score.
        print("Partie terminée !!")
        break # fin de la boucle
    print("Essayez encore !!")

