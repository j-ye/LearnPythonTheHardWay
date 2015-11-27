from sys import argv

script, filename = argv

target = open(filename)
line = target.read()

print(line)
