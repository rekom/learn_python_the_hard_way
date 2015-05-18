# ecrire une variable x avec ce string dedans :

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# ecrire une autre variable avec ce string et remplacer les 2 %s par binary et do_not
y = "Those who knows %s and those %s." % (binary, do_not)

# on printe les 2 variables
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?!"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e