name = 'Fabien'
age = 37 # not a lie
height = 74 # inches
weight = 180  # pounds
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

kg = weight / 2.2046
cm = height * 2.54

print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "He's %d cm tall." % cm
print "He's %d pounds heavy." % weight
print "He's %d kg heavy." % kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
    


