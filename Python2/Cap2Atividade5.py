num = int(input("digite seu numero: "))
for num in range(0, num):
 soma = 0

 t = num
 while t > 0:
   d = t % 10
   soma += d ** 3
   t //= 10

 if num == soma:
   print(num,"é um número Armstrong")
 else:
   print(num,"não é um número Armstrong")
