contatos = {
    "emanoel@gmail.com":{"nome":"Emanoel","telefone":"0000--0000"},
    "alice@gmail.com":{"nome":"alice","telefone":"1111--0000"},
    "tiago@gmail.com":{"nome":"tiago","telefone":"0000--1111"},
    "simone@gmail.com":{"nome":"simone","telefone":"4444--0000"},
    "adailton@gmail.com":{"nome":"adailton","telefone":"5555--0000"}
}

print(contatos["emanoel@gmail.com"]["telefone"])
print()

for chave,valor in contatos.items():
    print(chave,valor)

print()