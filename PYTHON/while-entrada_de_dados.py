codigo=-1
while codigo!=0:
    codigo = int(input("Informe o código:"))
    if codigo!=0:
        notal = float(input("Informe a primeira nota: "))
        nota2 = float(input("Informe a segunda nota: "))
        nota3 = float(input("Informe a terceira nota: "))

        media=(notal+nota2+nota3)/3

        print(f"Código:{codigo} -> Média: {media}")
                                    