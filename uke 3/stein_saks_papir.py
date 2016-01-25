import random
print "Velg STEIN, SAKS eller PAPIR"


choices = ["STEIN", "SAKS", "PAPIR"]
choices1 = ["STEIN", "SAKS", "PAPIR"]


p1 = "player one rolls:"
p2 = "player two rolls:"

print p1, (choices[random.randint(0,2)])
choices = (choices[random.randint(0,2)])
print "VS"
choices1 = (choices1[random.randint(0,2)])
print p2, (choices1[random.randint(0,2)])

if choices == choices1:
    print "Draw!"
    

 