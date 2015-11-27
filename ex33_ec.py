def add_number(i, numbers, increment):
    while i < 10:
        print("At the top i is %d" %i)
        numbers.append(i)

        i += increment
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)


    print("The numbers: ")

    for num in numbers:
        print(num)

num = []
add_number(0, num, 0.5)



# new
elements = []
for num in range(0, 6):
    elements.append(num)
    
print(elements)
