# Use the file name mbox-short.txt as the file name
# fname = raw_input("Enter file name: ")
# fh = open(fname)
fh = open('mbox-short.txt')
count = 0
sum = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
#    print pos
#     print line[pos+1:]
    chop = (line[pos+1:])
#     print chop
    
    if chop.startswith(' 0.') :
        count = count + 1
    chop = float(chop)
    sum = sum + chop
# print count
# print sum

avg = sum/count

print 'Average spam confidence',avg



# print "Done"