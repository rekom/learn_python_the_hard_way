# -*- coding: utf-8 -*- 

from sys import exit
import random
str = 0
int = 0
bag =[]
runesread = False

def start():
    global str
    global int
    global bag
    print """Vous allez créer votre personnage
Celui-ci dispose de deux caractéristiques principales 
la Force et l'Intelligence"""
    
    raw_input("Lancer 3d6 pour connaitre votre score d'intelligence en appuyant sur enter ")
    int = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    print "Votre score d'intelligence est de %s" % int
    choixint = raw_input("Etes vous satisfait de votre score d'intelligence (vous avez droit à un autre jet? et on garde le meilleur) \n")

    if choixint == "oui" :
        choixint = int
        print "Votre score d'intelligence définitif est de %s" % int
    elif choixint == "non" :
        raw_input("Lancer 3d6 pour connaitre votre score d'intelligence en appuyant sur enter  ")
        int2 = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        print "Votre nouveau score d'intelligence est de %s" % int2
        if int > int2 :
            int = int
            print "Votre score final d'intelligence est de %s" % int
        elif int < int2 :
            int = int2
            print "Votre score final d'intelligence est de %s" % int
        else :
            print "\nMerci de répondre à la question"
            start()
    else :
        print "Merci de répondre à la question"
        start()
    
    print """\nVous allez maintenant lancer les dés pour votre score de force"""
    
    raw_input("Lancer 3d6 pour connaitre votre score de force en appuyant sur enter ")
    str = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    print "Votre score de force est de %s" % str
    choixstr = raw_input("Etes vous satisfait de votre score de force? (vous avez droit à un autre jet et le meilleur est gardé) \n")
    
    if choixstr == "oui" :
        choixstr = str
        print "Votre score de force définitif est de %s" % str
    elif choixstr == "non" :
        raw_input("Lancer 3d6 pour connaitre votre score de force en appuyant sur enter  ")
        str2 = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        print "Votre nouveau score de force est de %s" % str2
        if str > str2 :
            str = str
            print "Votre score final de force est de %s" % str
        elif str < str2 :
            str = str2
            print "Votre score final de force est de %s" % str
        else :
            print "\nMerci de répondre à la question"
            start()
    else :
        print "Merci de répondre à la question"
        start()
    
    print "\nVotre force est de %s et votre intelligence de %s" % (str, int)
    bag = []
    
    print "Vous avez également un sac. Pour le moment celui ci contient %r" % bag
    room_01()
    
def room_01():
    global str
    global int
    global bag
    print """Vous entrez dans un labyrinthe. 
    \nDans la première salle se trouve deux portes à gauche et à droite ainsi qu’un tableau avec une série de runes"""
    room_1()
    
def room_1():
    global str
    global int
    global bag
    global runesread
    
    choixroom_1 = raw_input("Que faites-vous?  ")
    
    if choixroom_1 == "gauche" :
        room_2()
    elif choixroom_1 == "droite" :
        room_4()
    elif (choixroom_1 == "rune" or choixroom_1 == "runes" or choixroom_1 == "tableau") and runesread == False :
        print "Vous vous approchez des runes et remarquez qu'elles sont activables en pressant dessus"
        if int > 12 :
            print "Avec votre intelligence élevée, vous déchiffrez les runes et en appuyant dans l'ordre ouvrez un passage secret!"
            runesread = True
            room_secret()
        else: 
            print "Vous avez beau essayer d'appuyer sur les runes, il ne se passe rien, peut-être qu'en étant un peu plus intelligent vous auriez pu les déhiffrer"
            room_1()
    elif (choixroom_1 == "rune" or choixroom_1 == "runes" or choixroom_1 == "tableau") and runesread == True :
        print "Vous avez déjà appuyé sur les runes pour ouvrir le passage secret (vous pouvez vous rendre dans la pièce de droite ou de gauche)"
        room_1()
    else:
        print "Je n'ai pas compris"
        room_1()

def room_2():
    global str
    global int
    global bag
    levier = False
    print "Dans cette petite pièce, vous pouvez voir un bouton et un levier ainsi qu'une porte condamnée"
    print "La porte condamnée semble solide"
    
    if str > 16:
        print "Avec votre force surhumaine, vous arrivez à débloquer la porte sans toucher le levier"
        room_end()
    else:
        print "Vous n'êtes pas assez fort, il va falloir ouvrir la porte avec les leviers"
        
        while True :
            choix = raw_input("faites vous? > ")
            
            if choix == "bouton" and not levier :
                print "Il ne se passe rien"

            elif choix == "levier" :
                print "Le levier s'est abaissé"
                levier = True

            elif choix == "bouton" and levier == True:
                print "En appuyant sur le bouton une fois le levier abaissé, la porte s'ouvre"
                room_3()
            else:
                print "appuyer sur le bouton ou bouger le levier"
                room_2()

def room_3():
    global str
    global int
    global bag
    print "Dans cette pièce, il n'y a pas grand chose, vous trouvez un cochon en or que vous ramassez et mettez dans votre sac"
    bag.append("cochon")
    print "\nVous avez maintenant plusieurs objet dans votre sac dont  %s." % bag
    room_end()

def room_4():
    global str
    global int
    global bag
    gob = 10
    print "Dans cette pièce, vous vous retrouvez face à un gobelin"
    print "Celui-ci vous charge et vous ripostez"
    raw_input("Lancer 1d10 pour connaitre votre niveau d'attaque score de force en appuyant sur enter  ")
    force = random.randint(1,10)
    print "vous avez fait %s, auquel vous ajoutez votre force %s, pour une attaque totale de %s" % (force, str, (str+force))
    totattp = force + str
    forcegob = random.randint(1,10)
    print "le gobelin lui à %s en force et fait un jet de %s" % (gob, forcegob)
    totattg = forcegob + gob
    print "son score final est de %s" % (totattg)
    
    if totattp > totattg :
        print "le gobelin git dans son sang et vous vous rendez dans la prochaine salle"
        print "Vous trouvez un cochon en or dans le sac du gobelin que vous ramassez et mettez dans votre sac"
        bag.append("cochon")
        print "\nVous avez maintenant %r objet dans votre sac." % bag
        room_end()
    else :
        print "Vous etes mort tués par un gobelin"
        start()  
    

def room_end():
    global str
    global int
    global bag
    cochon = 50
    statuette = 100
    fric = 0
    print "Vous êtes dans la dernière pièce, nous allons compter combien vous allez"
    print "pouvoir tirer de votre sac qui contient %s." % bag
    if "statuette" and not "cochon" in bag :
        fric = fric + statuette
    elif "cochon" and not "statuette" in bag:
        fric = fric + cochon
    elif ("cochon" and "statuette") in bag:
        fric = cochon + statuette
    else:
        print "Vous n'avez rien dans votre sac!"
    print "Vous avez fini l'aventure avec %s gold bravo!" % fric
    
    
def room_secret():
    global str
    global int
    global bag
    global runesread
    print runesread
    print "Vous entrez dans une pièce secrète"
    print "\nDans cette pièce, vous trouvez une statuette en or que vous mettez dans votre sac."
    bag.append("statuette")
    print "\nVous avez maintenant un objet dans votre sac, une %s et vous décidez de revenir dans la salle des runes précédente et prendre la porte de droite ou de gauche." % bag
    room_1()
    
    
        
        
        
    

start()
    
    