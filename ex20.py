from sys import argv

script, input_file = argv   #asks for an input file when executing

def print_all(f):       #define print_all
    print(f.read())     #f is the file, f.read() reads the file, and prints out

def rewind(f):          #define rewind
    f.seek(0)           #sets the file's current position at the offset 0

def print_a_line(line_count, f):    #define print_a_line function
    print(line_count, f.readline()) #print out line number, and line

current_file = open(input_file)     #current_file is the opened file

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
