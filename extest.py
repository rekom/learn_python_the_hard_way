# -*- coding: utf-8 -*- 
bag =["cochon"]
cochon = 50
statuette = 100
harpe = 150
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
    
print fric