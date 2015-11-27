from sys import argv        #import argv

script, filename = argv     #feed filename while running the file

print("We're going to erase %r." % filename)   #print a line w/ file name
print("If you don't want that, hit CTRL-C (^C).") #print out two cases
print("If you do want that, hit RETURN.")

input("?") #asks for input. CTRL-C generates an error and ends the code.

print("Opening the file...") #print line
target = open(filename, 'w') #open file in write mode

print("Truncating the file. Goodbye!") #print line
target.truncate() #empties the file

print("Now I'm going to ask you for three lines.") #print line

line1 = input("line 1: ") #asks for user input
line2 = input("line 2: ") #asks for user input
line3 = input("line 3: ") #asks for user input

print("I'm going to write these to the file.") #print line

target.write(line1) #target is the opened file, .write() writes line1
target.write("\n")  #write new line
target.write(line2) #write line2
target.write("\n")  #write new line
target.write(line3) #write line3
target.write("\n")  #write new line

print("And finally, we close it.") #print line
target.close()      #close target, the opened file
