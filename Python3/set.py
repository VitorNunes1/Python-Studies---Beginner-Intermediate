list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

s1 = set(list1)
s2 = set(list2)

print()
print(s1|s2)
print(s1&s2)
print(s1-s2)
print(s2-s1)
print(s1^s2)
print(s1.intersection(s2))

