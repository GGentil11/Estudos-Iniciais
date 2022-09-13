tabuada = int(input("Insira o número: "))

for posicao in range (1,11):
    resultado = tabuada * posicao
    print(f"{tabuada} x {posicao} = {resultado}")