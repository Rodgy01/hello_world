#python random randrange() and randint to generate integer number within a range
import random
#1) lst = random.sample(range(0, 1000), 10) # returns a list of random numbers
pp = []
#2 random.randrange(100000, 1000000, 6) returns any random integer of specific length 3
for i in range(21):
    ID = "71-" + str(random.randrange(100000,1000000, 6)) +" "+ random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + "71"
    pp.append(ID)
print(pp)

#3 random.randint(0,9) returns any integer from 0 to 9
    