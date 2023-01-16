emails_senai = {
    "Centro": "centrosenai@sp.senai.br",
    "Anchieta": "anchieta@sp.senai.br",
    "ABC": "abc@sp.senai.br",
    "Osaco": "osasco@sp.senai.br"
}

#Selecionar um item do "dicionário"
set_email = emails_senai['Centro']
print(set_email)

#Adiciona um item ao dicionário existente
emails_senai["Campinas"] = "campinas@sp.senai.br"
print(emails_senai)

#Adiciona um item ao dicionário existente
emails_senai.setdefault("Limeira","limeira@sp.senai.br")
print(emails_senai)

#Atualizar um item ao dicionário existente
emails_senai["Anchieta"] = "saoanchietasp@sp.senai.sp"
print(emails_senai)

#Lista somente a chave - rótulos do dicionário linha a linha
print(emails_senai.keys())

#Lista somente os valores do dicionário linha a linha
print(emails_senai.values())

#Lista todos os itens do dicionário linha a linha
for i in emails_senai:
    print(i)

#Listar todos os itens o dicionário linha a linha
for i in emails_senai:
    print(emails_senai[i])

#Deletar um item do dicionário
emails_senai.pop("ABC")
print(emails_senai)

#Verificar a existência de um item do dicionário
if "ABC" in emails_senai:
    print(emails_senai[i])
else:
    print("Não existe!")