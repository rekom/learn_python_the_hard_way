# -*- coding: utf-8 -*-

from sys import argv

# on lance le script et l'argument devient une 
# variable input_file
script, input_file = argv

#1er def on lit le fichier
def print_all(f):
    print f.read()
    
# on fait un rewind on revient à la ligne 1    
def rewind(f):
    f.seek(0)

# on fait une autre fonction dans laquelle on passe 2
# arguments et on affiche la variable line_count et
# on lit la premier ligne

def print_a_line(line_count, f):
    print line_count, f.readline(),

# nouvelle varible ou on met le contenu du fichier du début

current_file = open(input_file)

print "First let's print the whole file:\n"

# appel de la fonction print_all dans laquelle on passe 
#la variable current file 

print_all(current_file)

print "Now let's rewind, kind of like a tape."

# on appelle la fonction rewind et on lit la ligne 1
rewind(current_file)

print "Let's print three line:"

# on cree une nouvelle variable pour conter
# et on passe la fonction print a line qui va afficher
# les lignes.

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)