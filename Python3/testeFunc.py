try:
    def myfunc(n):
        return lambda a : a * n

    def entrada():
        valor1 = int(input("Digite um número inteiro: "))
        valor2 = int(input("Digite um número inteiro: "))

        mydoubler = lambda x : x + valor1
        mytripler = myfunc(valor1)
        mysend = lambda x1, y1, z1: x1 * y1 + z1
        print(mysend(valor1, valor2, 3))
        print(mydoubler(valor1))
        print(mytripler(valor2))
        #print(mydoubler(valor1,5))
        #print(mydoubler(4))
        #print(mytripler(6))



        #mydoubler = myfunc(2)
        #mytripler = myfunc(3)
    def lambdaarray():
        a = [1, 2, 3, 4, 5, 6, 7]
        square_a = list(map(lambda x: x**2, a))
        print(square_a)
    entrada()

    lambdaarray()

except:
    print("Error!")