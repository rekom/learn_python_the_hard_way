# -*- coding: utf-8 -*- 
from sys import exit
import random

print "Vous allez créer votre personnage"
print "Celui-ci dispose de deux caractéristiques principales"
print "la Force et l'Intelligence"
raw_input("Lancer 3d6 pour connaitre votre score d'intelligence en appuyant sur enter ")
int = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

print int