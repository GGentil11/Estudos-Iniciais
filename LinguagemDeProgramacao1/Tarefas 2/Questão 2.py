import math

largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))

area = altura * largura
consumo = (0.3 * area)/ 2

print("Serão necessárias {} latas de tinta". format(math.ceil(consumo)))