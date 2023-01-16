mes = int(input("Saiba qual mês é pela numeração (1 à 12): "))
messa = ["Não existe mês 0", "janeiro", "fevereiro", "março", "abril","maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

if (mes > 12):
    print("Não existe mais que 12 meses !")
else:
    print(messa[mes])



