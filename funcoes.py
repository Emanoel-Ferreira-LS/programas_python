def ola_mundo():            #Função sem argumentos 
    print("Olá, Mundo!\n")

ola_mundo()                 #Chamada da função


def soma(*,n1,n2):
    result = n1*n2
    print("{} * {} = {}" .format(n1,n2,result))

def multiplicacao(n1,/,n2):
    result = n1*n2          
    print("{} * {} = {}".format(n1,n2,result))

def divisao(n1,n2):
    result = n1/n2
    print("{} / {} = {}".format(n1,n2,result))

def subtracao(n1,n2):
    result = n1-n2
    print("{} - {} = {}".format(n1,n2,result))

soma(n1=2,n2=3)
multiplicacao(10,n2=10)
divisao(10,2)
subtracao(50,25)









