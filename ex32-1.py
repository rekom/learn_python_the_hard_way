# -*- coding: utf-8 -*- 
import random

print "On va jouer à un jeu dont vous êtes le heros"
print "C'est un jeu classique dans lequel on fait des choix et qui font avancer dans le jeu."

print "Pour jouer un magicien, tapper 1, pour jouer un geurrier tapper 2."

joueur = raw_input("Choix du joueur > ")

if joueur == "1":
    joueur = "mago"
    print "Vous avez choisi de jouer un magicien"
elif joueur == "2":
    print "Vous avez choisi de jouer un guerrier"
    joueur = "fighter"
else:
    print "Ce n'est pas un joueur possible merci de recommencer"

if joueur == "mago":
    print "le magicien peut choisir un sort au choix "
    print "la boulle de feu, choix 1"
    print "l'éclair, choix 2"
    
    choix_sort = raw_input("Quel sort choisissez vous? > ")
    fireball = "Boule de feu"
    storm = "Eclair"
    
    if choix_sort == "1" :
        choix_sort = fireball
    elif choix_sort == "2":
        choix_sort = storm

    if choix_sort == fireball:
        print "Vous avez choisi %s et non pas l'éclair" % fireball
    elif choix_sort == storm:
        print "vous avez choisi %s et non pas la boulle de feu" % storm
elif joueur == "fighter": 
    print "Le guerrier peut choisir deux armes différentes"
    print "l'épée, choix 1"
    print "la hache, choix 2"
    
    choix_arme = raw_input("Quelle arme choississez vous? > ")
    sword = "Epée"
    axe = "La hache"
    if choix_arme == "1" :
        choix_arme = sword
    elif choix_arme == "2":
        choix_arme = axe

    if choix_arme == sword:
        print "Vous avez choisi %s et non pas la hache" % sword
    elif choix_arme == axe:
        print "vous avez choisi %s et non pas l'épée" % axe

print joueur
if joueur == "mago":
    print "Vous aller tirer maintenant votre caractéristiques d'intélligence"
    raw_input("Appuyer sur entrée pour tirer votre jet d'intelligence")
    int = random.randint(1,18)
    print "Votre intelligence est de %s" % int
    print "Etes vous satisfait de votre jet?"
    choix = raw_input("Oui ou non? > ")
    if choix == "oui":
        print "Votre intelligence est de %s" % int
        intelligence = int
    elif choix == "non":
        print "Deuxième jet possible, (le meilleur est gardé)"
        raw_input("Appuyer sur entrée pour tirer votre jet d'intelligence")
        int2 = random.randint(1,18)
        print "Votre intelligence est de %s" % int2
        if int > int2:
            intelligence = int
        else:
            intelligence = int2
    print "Votre score d'int définitif est %s" % intelligence

elif joueur == "fighter":
    print "On ne va pas jouer avec le geurrier"

if joueur == "mago":
    print "Vous allez devoir combattre des montres en psychic"
    monstre = random.randint(1,10)
    print "Le premier monstre à %s en psychic" % monstre
    print "voulez vous vous battre en psychic ou avec un sort? (vous avez %s en intelligence)" % intelligence
    battle = raw_input("Pour vous battre en intelligence tapper 1, pour vous battre avec un sort tappez 2 > ")
    if battle == "1":
        print "le psychic du montre est de %s, et votre intelligence est de %s" % (monstre, intelligence)
        if intelligence >= monstre:
            print "Vous remportez le combat!"
        else:
            print "Vous avez perdu vous êtes mort!"
    elif battle == "2":
        print "Vous lancez un sort et vous gagnez le combat!"
else:
    print "Finish"
    


        
        


 
 
        
    