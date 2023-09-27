lista = ["lista","python",False]
print(lista)

frutas = ["maça", "laranja", "goiaba"]
print(frutas[-1])
print(lista[-1])

numeros = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(numeros[0])
print(numeros[0][3])

#interar listas
for i in numeros:
    print(i)

#enumeração de elementos de uma lista
for indice,fruta in enumerate(frutas):
    print(f"{indice}:{fruta}")

#Compressão de lsitas
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
pares = []

for i in lista_numeros:
    if i % 2 == 0:
        pares.append(i)

print(pares)

#
impares = [i for i in lista_numeros if i % 2 == 1]
print(impares)

