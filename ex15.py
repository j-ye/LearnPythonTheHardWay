from sys import argv            #import argv

script, filename = argv         #user input filename

txt = open(filename)            #txt is the opened file

print("Here's your file %r:" % filename) #print a line telling you the file printing out
print(txt.read())               #txt is the opened doc. calls on .read() command

print("I'll also ask you to type it again:") #print line
file_again = input("> ")        #asks for user input, and stores as file_again

txt_again = open(file_again)    #txt_again is the opened file

print(txt_again.read())         #txt is the opened doc. calls on .read() command
