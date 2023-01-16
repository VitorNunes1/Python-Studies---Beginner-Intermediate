f = open("isthat.txt", "x") #Esse segundo é para mudar a execução de acordo com a existência do arquivo, o "X" por exemplo da erro quando o arquivo já existir, o "A" funciona. O "R" Lê o arquivo e traz para cá com:
#open(isthat.txt, "r") try: print(f.read())

try:
    f.write("Enter a text in firts line of the file\n")
    f.write("Test of enter\n")
    f.write("Words and informations\n")

finally:
    f.close()

#Vai inserir o código para o arquivo "isthat.txt"

