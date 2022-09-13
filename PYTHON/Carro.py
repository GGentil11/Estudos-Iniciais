precoFabrica = float(input("Informe o preço do carro: "))
lucroDistribuidor1 = float(input("Informe o percentual de lucro do distribuidor: "))
imposto1 = float(input("Informe o percentual de imposto do produto: "))

lucroDistribuidor2 = precoFabrica * lucroDistribuidor1 / 100 
imposto2 = precoFabrica * imposto1 / 100
precoFinal = precoFabrica + lucroDistribuidor2 + imposto2

print("\nLucro do distribuidor:{} \n" .format(lucroDistribuidor2))
print("\nValor do imposto:{} \n" .format (imposto2))
print("\nPreço final do carro:{} \n".format (precoFinal))