name = 'Zed A. Shaw'
age = 35
height = 74 #inches
height_cm = height * 2.5
weight = 180 #lb
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %r." % name)
print("He's %d inches tall, which is %d cm" % (height, height_cm))
print("He's %d pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

print("If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight))
