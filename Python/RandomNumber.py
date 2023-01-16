import random #Call a random number with (random)
number = random.randint(1, 100)
print(number)

#Cara ou coroa
coin = random.randrange(2)

print("Draw value")
if coin == 0:
    print("Front")
else:
    print("Back")

print("Finish game")