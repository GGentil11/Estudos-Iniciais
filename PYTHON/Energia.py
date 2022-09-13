salario = float (input('Qual o valor do salário mínimo?'))
energiaConsumo = float (input("Consumo de energia em quillowatts em sua residência: \n"))

precoQuilo = salario / 5
contaTotal = energiaConsumo * precoQuilo 
contaDesconto = contaTotal * 0.85

print("\nValor do quilowatt:\nR${} " .format(precoQuilo))
print("\nValor da conta de energia:\nR${} \n".format(contaTotal))
print("\nValor da conta de energia com desconto:\nR${} " .format (contaDesconto))