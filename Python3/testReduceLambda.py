from functools import reduce
    #Reduce serviria para redução das contas
    #x  y (Vai somar cada número do array)
a = [1, 2, 3, 4]
b = [1, 1, 1, 1]
n = reduce(lambda x, y: x + y, a)
i = reduce(lambda x, y: x + y, b)
print(n)
print(i)