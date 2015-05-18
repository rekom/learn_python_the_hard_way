name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dict = dict()
for line in handle:
    if not line.startswith('From '): continue
    spl = line.split()
    time = spl[5]
    time = time.split(":")
    hours = time[0]
    dict[hours] = dict.get(hours, 0) +1 

list = dict.items()
list.sort()
for key, val in list :
    print key, val