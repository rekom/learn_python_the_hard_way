def computegrade(score) :
    if score < 0 :
        grade = "Erreur, merci d'entrer un chiffre compris entre 0.0 et 1.0"
    if score > 1 : 
        grade = "Erreur, merci d'entrer un chiffre compris entre 0.0 et 1.0"
    elif type(score) == str :
        grade = "Bad score"
    else :
        if score < 0.6 :
            grade = "F"
        elif score >= 0.9 :
            grade = "A"
        elif score >= 0.8 :
            grade = "B"
        elif score >= 0.7 :
            grade = "C"
        elif score >= 0.6 :
            grade = "D"
    return grade 

try:
    score = raw_input("Entrez un chiffre compris entre 0.0 et 1.0: ")
    score = float(score)
except:
    print "Merci d'entrer un chiffre alpha numerique"
    quit()

grade = computegrade(score)
print grade