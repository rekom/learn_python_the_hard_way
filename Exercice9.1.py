fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
map = dict()

for line in fh :
    if not line.startswith('From ') : continue
    words = line.split()
    mail = words[1]
    map[mail] = map.get(mail, 0) +1 
    
bigcount = None
bigword = None

for key,value in map.items() :
    if value is None or value > bigcount :
        bigcount = value
        bigword = key
print bigword, bigcount