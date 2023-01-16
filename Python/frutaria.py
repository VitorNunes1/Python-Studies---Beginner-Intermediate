#Menu
print("Esta é a frutaria de David.")
print("---------------------------------")
print("1: Maçã( preço : 5 reais)")
print("2: Uva( preço : 6 reais)")
print("3: Melão( preço : 8 reais)")
print("4: Laranja( preço : 2 reais)")
print("---------------------------------")

#Recebendo os valores
fruta = int(input("Digite o número do item (entre 1~4)"))
quantidade = int(input("Digite o quantidade do item(entre 1~10)"))

#Verificar o item no menu e retorna no sistema
if ((fruta >= 1) and (fruta <= 4)):
    if(fruta ==1):
        txtfruta = "Maçã"
        preço = 5
    elif(fruta == 2):
        txtfruta = "Uva"
        preço = 6
    elif(fruta == 3):
        txtfruta = "Melão"
        preço = 8
    elif(fruta == 4):
        txtfruta = "Laranja"
        preço = 2
    
    calculo = quantidade * preço
    
    print("Frutas selecionadas :",txtfruta)
    print("Preço :",preço)
    print("Quantidade:", quantidade)
    print("O preço total é",calculo,"reais")
    print(f"O preço total deu {calculo} reais")

    #Pagamento das compras
    dinheiro = int(input("Inserir dinheiro por favor(ex: 15): "))

    if (dinheiro >= calculo):
        troco = dinheiro - calculo
        if troco > 0:
            print(f"Recebido {dinheiro} reais. Seu troco é de {troco} reais.")   
        else:
            print(f"Recebido {dinheiro} reais. Sem troco")   
    else:
        print("Valor digitando é menor que o total da compra")
    
else:
    print("Item digitando não existe no menu")