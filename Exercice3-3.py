try:
    score = raw_input("Entrez un chiffre compris entre 0.0 et 1.0: ")
    score = float(score)
except:
    print "Merci d'entrer un chiffre alpha numerique"
    quit()

if score < 0 : 
    print "Erreur, merci d'entrer un chiffre compris entre 0.0 et 1.0"
if score > 1 :
    print "Erreur, merci d'entrer un chiffre compris entre 0.0 et 1.0"
else :
    if score < 0.6 :
        print "F"
    elif score >= 0.9 :
        print "A"
    elif score >= 0.8 :
        print "B"
    elif score >= 0.7 :
        print "C"
    elif score >= 0.6 :
        print "D"