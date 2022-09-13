salarioBase = float(input("Digite o valor do salário base: "))

salarioGrat = float(salarioBase * 1.05)
salarioImposto = float(salarioBase * 0.93)
novoSalario = salarioGrat - salarioImposto
novissimoSalario = novoSalario + salarioBase

print('Novo salário:\nR${} ' .format (novissimoSalario))