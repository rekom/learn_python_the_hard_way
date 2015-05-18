try:
    hrs = float(raw_input("Enter Hours:"))
    rte = float(raw_input("Enter Rate:"))
    
except:
    print "Error, please enter numeric input"
    quit()
    
print rte, hrs
if hrs <= 40:
    pay = (hrs*rte)
elif hrs > 40:
    pay = (40*rte)+((hrs-40)*(rte*1.5))
print pay


# pay = round(float(hrs)*float(rte), 2)

# print pay
