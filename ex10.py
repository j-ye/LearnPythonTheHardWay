tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
blackslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(blackslash_cat)
print(fat_cat)

cat1 = "I'm \a a %s." % tabby_cat
cat2 = "I'm \a a %r." % tabby_cat
print(cat1)
print(cat2)
