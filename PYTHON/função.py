def ler_Notas():
    n = float(input("Digite uma nota para o aluno: "))
    return n

def resultado(n1, n2):
    media = (n1 + n2)/ 2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Média: ", media, "\n", "Resultado: ", end = "")

    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

a = ler_Notas()
b = ler_Notas()
resultado(a, b)