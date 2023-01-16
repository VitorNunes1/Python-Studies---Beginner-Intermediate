import random

randomtest=int(input("Enter a number until 100: "))

while True:
    random_integer = random.randint(1, 100)
    print(random_integer)
    if random_integer == randomtest:
        break