import os

def limpar():
    os.system('cls')

limpar()
nota100 = int(input("Informe a quantidade de notas de 100 reais que você possui: "))
nota50 = int(input("Informe a quantidade de notas de 50 reais que você possui: "))
nota10 = int(input("Informe a quantidade de notas de 10 reais que você possui: "))
nota5 = int(input("Informe a quantidade de notas de 5 reais que você possui: "))
nota1 = int(input("Informe a quantidade de moedas de 1 reais que você possui: "))

montante = (100 * nota100) + (50 * nota50) + (10 * nota10) + (5 * nota5) + (1 * nota1)

limpar()
print("Montante de dinheiro calculado: R${}".format(montante))