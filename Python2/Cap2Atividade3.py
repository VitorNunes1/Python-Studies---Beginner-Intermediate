SIC1 = int(input("Você é maior de idade? (digite 1 se sim, 0 se não): "))
SIC2 = int(input("Você é casado(a)? (digite 1 se sim, 0 se não): "))

if (SIC1 == 1 and SIC2 == 1):
    print("Você é maior de idade e casado(a).")
elif (SIC1 == 0 and SIC2 == 0):
    print("Você não é menor de idade e solteiro(a).")
elif (SIC1 == 0 and SIC2 == 1):
    print("Você é menor de idade e é casado(a).")
elif (SIC1 == 1 and SIC2 == 0):
    print("Você é maior de idade e não é casado.")
else:
    print("ERRO. Digite 1 ou 0 para validar as respostas.")
