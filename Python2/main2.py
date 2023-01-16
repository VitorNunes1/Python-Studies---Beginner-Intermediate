f = open("isthat.txt", "w")

try:
    for _ in range(5):
        n = input("Insira o número inteiro:")
        f.write(n)
        f.write('\n')

finally:
    f.close()
