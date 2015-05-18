# -*- coding: utf-8 -*-

# definition de la fonctuon cheese_and_crackers a laquelle on ajoute deux arg
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# On affiches l'arg cheese
    print "You have %d cheeses!" % cheese_count
# on affiche l'arg box of cracker
    print "You have %d box of crackers!" % boxes_of_crackers
    print "Man that's enough for a party"
    print "Get a blanket.\n"

# On lance la fonction en passant àes chiffres a la place des arguments    
print "we can just five the function àààààààààà numbers directly:"
cheese_and_crackers(20, 30)

# Ou alors on définit deux variables associées a des chiffres.
print "Or we can use varibale form our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# Puis on passe ces varibales dans la focntions
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# On peut egalement faire passer des maths dans la fonction des trucs de base.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# et on peut combiner les deux
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def pomme_et_poire(nombre_de_pommes, nombre_de_poires):
    print "Tu as %r pommes" % nombre_de_pommes
    print "Tu as %r poires" % nombre_de_poires
    
print "j'appelle la fonction avec des chiffres"
pomme_et_poire(15, 20)

print "Je m'appuie sur des variables"
pomme = 50
poire = 60

pomme_et_poire(pomme, poire)

print "Je multiplie les pommes avec les poires des variables"
pomme_et_poire(pomme*poire, pomme+poire)

print "Je passe une fonction dans la fonction?"
pomme_et_poire(pomme_et_poire, pomme_et_poire)

print "je passe le resultat de la fonction dans une variable"
total = pomme_et_poire(50, 100)
print "Voila mon %r total de fruit" % total

print "Entrer le nombre de pomme"
pomme = raw_input(">> ")

print "Entrer le nombre de poire"
poire = raw_input(">> ")

print "nombre de %s" % pomme
print "nombre de %s" % poire

print "One le passe dans la fonction"
pomme_et_poire(pomme, poire)


