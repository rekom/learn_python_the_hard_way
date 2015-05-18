tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

new_cat = "\tGros chat avec %s, %r" % (backslash_cat, persian_cat)

print new_cat

gros_cat = '''
\t*Chat sur une line\net sur une deuixeme
%r
''' % persian_cat

print gros_cat