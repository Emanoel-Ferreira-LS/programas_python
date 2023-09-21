opcao = -1

while opcao != 0:
    opcao = int(input("[1] Extrato \n[2] Sacar \n[0] Sair \n"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else: 
    print("Obrigado por usar o nosso sistema bancário, até logo!")