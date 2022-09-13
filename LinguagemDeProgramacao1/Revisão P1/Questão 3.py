tabuada = int(input("Insira o número: "))
while tabuada > 0 and tabuada < 10:
    for posicao in range (1,11):
        resultado = tabuada * posicao
        print(f"{tabuada} x {posicao} = {resultado}")
    break