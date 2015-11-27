from sys import exit
from sys import argv

script, name = argv

def door1():
    print("You have encountered the Cookie Monsters.")
    print("How many cookies do you take away from him?")

    next = int(input("> "))
    if next < 10:
        print("Nice. You are not greedy.")
        print("Let's count the cookies.")

        cookies = []
        i = 0
        while i <= next:
            cookies.append(i)
            print("Cookies count now:", cookies)
            i += 1

        print("%s, You win!" % name)
    else:
        dead("%s, Too greedy." % name)


#def door2():
#def door3():

def start():
    print("Welcome to the game. %s" % name)
    print("%s, You have 3 doors in front of you. Which one do you choose?" % name)

    next = int(input("> "))
    if next == 1:
        door1()
    elif next == 2:
        door2()
    elif next == 3:
        door3()
    else:
        dead("Jeez! Learn to type a number.")

def dead(why):
    print(why, "So Sad. Game over. :(")
    exit(0)

start()
