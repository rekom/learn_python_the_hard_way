print "You enter a dark room witj two doors. Do yoi get through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese caje. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "the bear eats your face off. Good Job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bears runs away." % bear
    
elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothspins."
    print "3. Understanding revolvers melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your bordu survives powered by a mind of jello. Good job!"
    else:
        print "the insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall o a knife and die. Good job!"
    
