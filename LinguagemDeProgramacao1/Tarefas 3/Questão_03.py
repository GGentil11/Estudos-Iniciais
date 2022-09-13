import string
import os

def limpar():
    os.system('cls')

limpar()
titulo = (input("Informe o Título: "))
caracteres = len(titulo)

bordaHorizontal = (caracteres * 2) * "-"
vertice = "+"
bordaVertical = "|"

limpar()

print(vertice.ljust(1),bordaHorizontal,vertice.rjust(1))
print(bordaVertical.ljust(1),titulo.center(caracteres * 2), bordaVertical.rjust(1))
print(vertice.ljust(1),bordaHorizontal,vertice.rjust(1))