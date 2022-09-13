import os
import time

def limpar():
    os.system('cls')

def fim():
    print("Encerrando operações...")
    time.sleep(2)
    limpar()  

def par_impar():
    limpar()
    quantidade = float(input("Informe quantas entradas você deseja adicionar: "))
    limpar()
    n = 0
    while n != quantidade:
        n += 1
        numero = float(input("Informe o número: "))
        if numero % 2 == 0:
            print("O número é par")
            time.sleep(2)
            limpar()
        else:
            print("O número é ímpar")
            time.sleep(2)
            limpar()
par_impar()
fim()