#importer le module argv
from sys import argv

#definir le module argv qui va avoir deux value a unpack
script, filename = argv

#on met dans une variable txt l'ouverture du fichier choisi au moment du unpack
txt = open(filename)

# on affiche le nom du fichier ouvert
print "Here's your file %r:" % filename

# on affiche le contenu de la variable txt
print txt.read()
txt.close()


print "type the filename again:"

#on definit une nouvelle variable dans laquelle on invite l'utilisateur a rentrer
#le meme nom de fichier que precedement
file_again = raw_input("> ")

# on ouvre le fichier encore une fois
txt_again = open(file_again)

# et on l'affiche a l'ecran
print txt_again.read()
txt_again.close()

