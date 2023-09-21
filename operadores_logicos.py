#No AND todos tem que ser True pra o resultado ser True
print(True and True)
print(True or True)
print(True or False)

#No OR basta um ser True e o resultado tambem será
print(True and False)
print(False and False)
print(False or False)
print("Verificar Conta")
saldo = 1000
saque = 250
limite = 200
conta_especial = True

conta_normal_saldo_suficiente = saldo >= saque and saque <= limite 
conta_especial_saldo_suficiente = conta_especial and saldo >= saque

expres_3 = conta_normal_saldo_suficiente or conta_especial_saldo_suficiente

print(expres_3)