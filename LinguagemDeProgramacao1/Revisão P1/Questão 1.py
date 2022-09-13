import os

def limpar():
    os.system('cls')

limpar()
primeiroNum = int(input("Informe o primeiro número: "))
segundoNum = int(input("Informe o segundo número: "))

def somar():
    soma = primeiroNum + segundoNum
    print("A soma é igual a: {}".format(soma))

def dobrar():
    dobro = 2 * (primeiroNum + segundoNum)
    print("O dobro da soma é igual a: {}".format(dobro))

def triplicar():
    triplo = 3 * (primeiroNum + segundoNum)
    print("O triplo da soma é igual a: {}".format(triplo))
    
somar()
dobrar()
triplicar()