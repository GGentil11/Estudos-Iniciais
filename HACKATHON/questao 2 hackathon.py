import numpy as np

vet_1 = []
def dividir (vet_1, n):
    for i in range(0, len(vet_1),n):
        yield vet_1[i:i+n]
x = 0
while True:
    while len(vet_1) == x:
        number = int(input("Insira os números: "))
        vet_1.append(number)
        x+=1
        n = 2
        dividir(vet_1, n)
        opcao = input("Deseja finalizar? (S ou N): ").upper()
        if opcao == "S":
            divisao = list(dividir(vet_1, n))
            print(divisao)
            print(abs(number))
            break 
        else:
            continue