valorHora = float(input("Informe o valor da hora:\nR$"))
aulas = int(input("Informe o número de aulas:\n"))
percentualDesconto = float(input("Informe o percentual de desconto do INSS:\n"))

salarioBruto = valorHora * aulas
valorDesconto = salarioBruto * percentualDesconto / 100
salarioLiquido = salarioBruto - valorDesconto

print("\nO salário líquido do professor é:\nR${}" .format (salarioLiquido))