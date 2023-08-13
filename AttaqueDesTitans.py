#coding:utf-8

"""
Exercice Python
> Créer un programme simulant un combat qui respecte les contraintes suivantes :
 - Deux joueurs, auxquels on demandera de choisir un pseudo
 - Les deux combattants démarrent avec 250 points de vie chacun
 - Le combat se déroule en quatre attaques (Joueur1, Joueur2, Joueur1 et enfin Joueur2)
 - Chaque attaque est une tentative (si elle réussit, le joueur infligera un nombre de dégats entre 0 et 100 et si elle
                                    si elle échoue, l'attaque est ratée, et c'est au tour de l'autre joueur)
 - A la fin du combat (4 attaques), on déclare le gagnant (celui à qui il reste le plus de points de vie)

 > Indications :
    - Le déroulement du combat doit être logique et annoncé à l'utilisateur (afficher du texte, décriver ce qu'il se passe)
    - Coder dans un premier temps uniquement avec affichages/saisies, variables, opérations, conditions.
    - Pour les plus avancées, vous pourrez optimiser ce code ensuite en l'adaptant avec vos connaissances (boucles,fonctions,
    classes etc...)
"""

import random

random_attack = True
random_damage = random.randint(0, 100)

Joueur1 = ""
Joueur2= ""

Joueur1 = input("Joueur 1, choisissez un pseudo : ")
Joueur2= input("Joueur 2, choisissez un pseudo : ")

Joueur1_pv = 250
Joueur2_pv = 250

random_attack = random.randint(0, 1)
random_attack = bool(random_attack)



print("\nLE COMBAT COMMENCE !\n")

#----------------------------------------------------------------------------------------------
#1ere attaque

input("Appuyez sur la touche 'Entrée' pour continuer...")
print("{} débute avec {} points de vie et {} débute avec {} points de vie.".format(Joueur1, Joueur1_pv, Joueur2, Joueur2_pv))

if random_attack == True:
    random_damage = random.randint(0, 100)
    Joueur2_pv = Joueur2_pv - random_damage
    print("{} attaque violemment {} et lui inflige {} de dégats !!".format(Joueur1, Joueur2, random_damage))

else:
    print("L'attaque de {} a lamentablement échouée...".format(Joueur1))

#-----------------------------------------------------------------------------------------------------------------------
#2éme attaque

input("Appuyez sur la touche 'Entrée' pour continuer...")
print("{} a {} points de vie et {} a {} points de vie.".format(Joueur1, Joueur1_pv, Joueur2, Joueur2_pv))

if random_attack == True:
    random_damage = random.randint(0, 100)
    Joueur1_pv = Joueur1_pv - random_damage
    print("{} attaque violemment {} et lui inflige {} de dégats !!".format(Joueur2, Joueur1, random_damage))

else:
    print("L'attaque de {} a lamentablement échouée...".format(Joueur2))

#-----------------------------------------------------------------------------------------------------------------------
#3éme attaque

input("Appuyez sur la touche 'Entrée' pour continuer...")
print("{} a {} points de vie et {} a {} points de vie.".format(Joueur1, Joueur1_pv, Joueur2, Joueur2_pv))

if random_attack == True:
    random_damage = random.randint(0, 100)
    Joueur2_pv = Joueur2_pv - random_damage
    print("{} attaque violemment {} et lui inflige {} de dégats !!".format(Joueur1, Joueur2, random_damage))

else:
    print("L'attaque de {} a lamentablement échouée...".format(Joueur1))

#-----------------------------------------------------------------------------------------------------------------------
#4éme attaque

input("Appuyez sur la touche 'Entrée' pour continuer...")
print("{} a {} points de vie et {} a {} points de vie.".format(Joueur1, Joueur1_pv, Joueur2, Joueur2_pv))

if random_attack == True:
    random_damage = random.randint(0, 100)
    Joueur1_pv = Joueur1_pv - random_damage
    print("{} attaque violemment {} et lui inflige {} de dégats !!".format(Joueur2, Joueur1, random_damage))

else:
    print("L'attaque de {} a lamentablement échouée...".format(Joueur2))

#-----------------------------------------------------------------------------------------------------------------------

if Joueur1_pv > Joueur2_pv:
    print("{} remporte la victoire avec {} points de vie restants.".format(Joueur1, Joueur1_pv))
    print("Encore bien joué et à la prochaine !")
elif Joueur2_pv < Joueur1_pv:
    print("{} remporte la victoire avec {} points de vie restants.".format(Joueur2, Joueur2_pv))
    print("Encore bien joué et à la prochaine !")
else:
    print("Match nul !")
    print("Encore bien joué et à la prochaine !")