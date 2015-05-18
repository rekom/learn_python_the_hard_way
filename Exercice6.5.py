text = "X-DSPAM-Confidence:    0.8475"
zeropos = text.find('0')
cinqpos = text.find('5')
num = text[zeropos : cinqpos+1]
solution = float(num)
print solution


