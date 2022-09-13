altura = float(input("Informe a altura (m): "))
peso = float(input("Informe o peso (kg): "))

imc = peso / altura**2
imc2 = 18.5
imc3 = 25
peso1 = imc2 * altura**2
peso2 = imc3 * altura**2

print("\nSeu IMC é de: {}" .format(round(imc, 2)))

if (imc < 15):
	print("Extremamente abaixo do peso")
elif (imc > 15 and imc <= 16):
	print("Gravemente abaixo do peso")
elif (imc > 16.5 and imc <= 18.5):
	print("Abaixo do peso ideal")
elif (imc > 18.5 and imc <= 25):
	print("Faixa de peso ideal")
elif (imc > 25 and imc <= 30):
	print("Sobrepeso")
elif (imc > 30 and imc <= 35):
	print("Obesidade grau I")
elif (imc > 35 and imc <= 40):
	print("Obesidade grau II (grave)")
elif (imc > 40):
	print("Obesidade grau III (mórbida)")

if (imc < 18.5 or imc> 25):
	print("Seu peso ideal é entre {}kg e {}kg".format(round(peso1, 2), round(peso2, 2)))