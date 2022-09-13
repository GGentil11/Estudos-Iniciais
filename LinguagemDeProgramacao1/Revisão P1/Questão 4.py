import os

def limpar():
    os.system('cls')

def par_impar():
    limpar()  
    numero = float(input("Insira o número: "))

    if numero % 2 == 0:
        print("O número {} é par".format(numero))
    else:
        print("O número {} é ímpar".format(numero))
par_impar()