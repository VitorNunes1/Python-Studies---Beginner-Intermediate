import random

conj1 = []
conj2 = []


for a in range (1, 7):
    test1 = random.randint(1,10)
    while test1 in conj1:
        test1 = random.randint(1,10)
    test2 = random.randint(1,10)
    while test2 in conj2:
        test2 = random.randint(1,10)
    conj1.append(test1)
    conj2.append(test2)

print()

test1 = set(conj1)
test2 = set(conj2)

print(test1, test2)
print(test1&test2)
print(test1|test2)
print(test1.intersection(test2))
print(test1-test2)
print(test2-test1)
print(test1^test2)