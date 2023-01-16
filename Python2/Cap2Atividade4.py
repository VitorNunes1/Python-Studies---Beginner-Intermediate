SICinput = int(input("Digite um número de 2 à 12 para saber se é primo ou composto: "))

SIC1 = [2, 3, 5 , 7, 11]
SIC2 = [4, 6, 8 ,9, 10, 12]

if (SIC1):
    print("O número",SICinput,"é um número primo")
elif (SIC2):
    print("O número",SICinput,"é um número composto")
else:
    print("Número inválido. Tente digitar um número de 2 à 12.")

