# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2, arg3 = args
    print "arg1 : %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3)
    
# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2, pipo):
    print "arg1 : %r, arg2: %r, pipo: %r" % (arg1, arg2, pipo)
    
# This one takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1
    
# this one takes no arguments
def print_none():
    print "I got nothin'"
    
    

print_two("Zed", "Shaw", "Pipo")
print_two_again("Zed", "Shaw", "tarace")
print_one("One!")
print_none()

    