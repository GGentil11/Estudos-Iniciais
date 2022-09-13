from re import S
from unittest import result


i = 0
qtdSexoF = 0
qtdSexoM = 0
somaIdadeMascExp = 0
qtdMasExp = 0
qtdMasc45 = 0
qtdFem21Exp = 0
menorIdadeFemExp = 0

qtdCandidatos = int(input("Quantidade de Candidatos: "))

for i in range(1, qtdCandidatos):
    print("\n", "Dados do Candidato {}" .format(i), "\n")
    idade = input("Informe a idade: ")
    sexo = input("Informe o sexo (M ou F): ")
    experiencia = input ("Possui experiência (S ou N): ")
S
    if (sexo == "M"):
        qtdSexoM += 1
        if (experiencia == "S"):
            somaIdadeMascExp += int(idade)S
            qtdMasExp += 1
        
        if (idade >= 45):
            qtdMasc45 += 1
        
    elif (sexo == "F"):
        qtdSexoF += 1
        if (idade < 21 and experiencia == "S"):
            qtdFem21Exp += 1
            if (menorIdadeFemExp == 0 or idade < menorIdadeFemExp):
                menorIdadeFemExp = idade
    
    print("\n", "Candidatos do sexo masculino: {}" .format(qtdSexoM))
    print("\n", "Candidatos do sexo feminino: {}" .format(qtdSexoF))
    if (qtdMascExp > 0):
        print("Idade média dos homens que já têm experiência no serviço: {}\n" .format(somaIdadeMascExp))
    if (qtdMascExp == 0):
        print("Idade média dos homen que já têm experiência no serviço: Não se aplica\n")
    
    if (qtdSexoM > 0):
        print("Percentual de homens com mais de 45 anos: {}\n" .format(qtdMasc45 * 1.0 / qtdSexoM * 100.0))  
    else:
        print("Homens com mais de 45 anos entre o total de homens: 0.0%\n")
        print("Mulheres com idade inferior a 21 anos e com esperiência no serviço: {}\n" .format(qtdFem21Exp))
        print("Menor idade entre as mulheres que já têm experiência no serviço: {}\n" .format(menorIdadeFemExp))
