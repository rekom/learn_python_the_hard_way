fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	wsp = line.rstrip()
	exo = wsp.split()
        for wrd in exo:
            if wrd in lst:
                continue
            else :
                lst.append(wrd)
lst.sort()
print lst
        