def computepay(h, r) :
    # print r, h
    if h <= 40:
        p = (h*r)
    elif h > 40:
        p = (40*r)+((h-40)*(r*1.5))
    # print p
    return p

try:
    hrs = float(raw_input("Enter Hours:"))
    rte = float(raw_input("Enter Rate:"))
    
except:
    print "Error, please enter numeric input"
    quit()

pay = computepay(hrs, rte)
print pay


# pay = round(float(hrs)*float(rte), 2)

# print pay
