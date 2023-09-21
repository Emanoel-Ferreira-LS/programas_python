if 2 < 4:
    print("2 < 4")

v1 = 4
v2 = 6

if v1 < v2:
    print("Valor 2 é maior que valor 1")
else:
    print("Valor 2 não é maior que valor 1")


MAIOR_IDADE = 18

idade = int(input("Informe sua idade:"))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")
elif idade > 0 and idade < 18:
    print("Menor de idade, não pode tirar CNH!")
else:
    print("Idade invalida!")

    