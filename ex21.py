def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

    
print "Let's do some math with just functions!"

x = float(raw_input("Quel est ton age? "))
z = float(raw_input("Quel est l'age de ta soeur? "))

age = add(x, z)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age : %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# a Puzzle for the extra credit, type it in anyway

print "Here's the puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"


test2 = 35 + (74 - (180 * (50/2)))

solution = age + (height - (weight * (iq/2)))

print solution

print test2

what2 = multiply(add(age, subtract(weight, (divide(weight,height)))), 2)

solution2 = ((((weight/height)-weight)+age)*2)
solution3 = (age+(weight-(weight/height)))*2
print what2

print solution2
print solution3