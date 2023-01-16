list = [5, 6, 3, 9, 2, 12, 3, 8, 7]

for i in range(0, len(list)):
    if (list[i] > list[len(list)-1]):
        list[i], list[len(list)-1] = list[len(list)-1], list[i]

print(list)