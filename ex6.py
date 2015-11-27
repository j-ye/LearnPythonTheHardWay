#define a string x, with formatted variable 10
x = "There are %d types of people." % 10

#define a string binary and do_not
binary = "binary"
do_not = "don't"

#define a string with two formatted variables. Included in parenthesis, which refer to the strings defined
y = "Those who know %s and those who %s." %(binary, do_not) #1: string within string

#print the two strings defined
print(x)
print(y)

#print string with a formatted variable, which is x
print("I said: %r." % x) #2: string within string
#print string with a formatted string, which is y. NOTE '%s'
print("I also said: '%s'." % y) #3: string within string

#define boolean
hilarious = False
#string with formatted variable, which is %r. But not specified
joke_evaluation = "Isn't that joke so funny?! %r" #4: string within a string

#print string, with formatted variable defined here.
print(joke_evaluation %hilarious)

#define two strings
w = "This is the left side of..."
e = "a string with a right side."

#concatenation
print(w + e)


#EC3: How do you know there are only four places? Look at %s and %r
#EC4: concatenation
