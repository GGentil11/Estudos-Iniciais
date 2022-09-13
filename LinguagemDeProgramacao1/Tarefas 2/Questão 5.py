import os

def limpar():
    os.system('cls')
limpar()
numero = int(input('Valor para sacar [10-600]: '))

while numero >= 10 and numero <= 600:
    nota100 = int(numero / 100)
    numero = numero % 100
        
    nota50 = int(numero/50)
    numero = numero % 50

    nota10 = int(numero/10)
    numero = numero % 10

    nota5 = int(numero/5)
    numero = numero % 5

    nota1 = numero
        
    limpar()
    print('Notas R$100,00 = ',nota100)
    print('Notas R$ 50,00 = ',nota50)
    print('Notas R$ 10,00 = ',nota10)
    print('Notas R$  5,00 = ',nota5)
    print('Notas R$  1,00 = ',nota1)