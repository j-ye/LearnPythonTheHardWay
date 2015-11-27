from sys import argv

script, user_name, adj = argv
answer = '>  '

print("Hi %s %s, I'm the %s script." % (adj, user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s %s?" % (adj, user_name))
likes = input(answer)

print("Where do you live %s %s?" % (adj, user_name))
lives = input(answer)

print("What kind of computer do you have?")
computer = input(answer)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))

#print(""" blah blah """ % formatter)
