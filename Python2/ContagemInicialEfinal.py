entrada = input("Número do horário inicial: ")
entrada2 = input("Número do término: ")
inicio, final = entrada, entrada2
inicio = int(inicio)
final = int(final)

finalmaior = final - inicio
igual = final == inicio
iniciomaior = (24 - inicio ) + final

if(entrada, entrada2 == finalmaior):
    print(f"DUROU {finalmaior} HORA(S)")
elif(entrada, entrada2 == igual):
    print(f"DUROU {igual} HORA(S)")
else:
    print(f"DUROU {iniciomaior} HORA(S)")