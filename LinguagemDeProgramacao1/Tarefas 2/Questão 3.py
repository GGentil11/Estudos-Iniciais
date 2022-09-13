import os

def limpar():
    os.system('cls')

limpar()  
nome = input("Informe o seu nome: ")
salario = float(input("Informe o valor do salário mínimo: "))
qtdeSalario = float(input("Informe a quantidade de salários que você recebeu: "))

salarioBruto = salario * qtdeSalario
salarioLiquido = salarioBruto - (0.3 * salarioBruto)

limpar()
print("Funcionário {}.\n"
      "O seu Salário Bruto é de: {}\n"
      "O seu Salário Líquido é de: {}".format(nome, salarioBruto, salarioLiquido))