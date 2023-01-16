#Criar uma lista em forma de rotulagem para outra lista
centro_teste = {
    "a": "testeA",
    "b": "testeB"
}

emails_senai = {
    "Centro": centro_teste,
    "Anchieta": "anchieta@sp.senai.br",
    "ABC": "abc@sp.senai.br",
    "Osaco": "osasco@sp.senai.br"
}

set_email = emails_senai['Centro']["a"]
print(set_email)
