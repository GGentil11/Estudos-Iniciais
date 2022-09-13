import os
import time
def limpar():
    os.system('cls')

limpar()
precoCarro = float(input("Informe o preço do carro: R$"))
limpar()
print("Gerando tabela...")
time.sleep (1.5)
print("    ================TABELA DE PREÇOS================","\n",
"QUANTIDADE DE PARCELAS  |  ACRÉSCIMO SOBRE O PREÇO FINAL","\n",
"==========6===========  |  =============3%==============","\n",
"==========12==========  |  =============6%==============","\n",
"==========18==========  |  =============9%==============","\n",
"==========24==========  |  =============12%=============","\n",
"==========30==========  |  =============15%=============","\n",
"==========36==========  |  =============18%=============","\n",
"==========42==========  |  =============21%=============","\n",
"==========48==========  |  =============24%=============","\n",
"==========54==========  |  =============27%=============","\n",
"==========60==========  |  =============30%=============","\n",)
parcelas = int(input("Informe o número de parcelas: "))
    
def valor():
    print(f"Preço final do carro: R${round(novoPreco, 2)}")
    print(f"Valor de cada parcela: R${round(novoPreco / parcelas, 2)}")

if parcelas == 6:
    novoPreco = precoCarro * 1.03
    limpar()
    valor()
elif parcelas == 12:
    novoPreco = precoCarro * 1.06
    limpar()
    valor()
elif parcelas == 18:
    novoPreco = precoCarro * 1.09
    limpar()
    valor()
elif parcelas == 24:
    novoPreco = precoCarro * 1.12
    limpar()
    valor()
elif parcelas == 30:
    novoPreco = precoCarro * 1.15
    limpar()
    valor()
elif parcelas == 36:
    novoPreco = precoCarro * 1.18
    limpar()
    valor()
elif parcelas == 42:
    novoPreco = precoCarro * 1.21
    limpar()
    valor()
elif parcelas == 48:
    novoPreco = precoCarro * 1.24
    limpar()
    valor()
elif parcelas == 54:
    novoPreco = precoCarro * 1.27
    limpar()
    valor()
elif parcelas == 60:
    novoPreco = precoCarro * 1.30
    limpar()
    valor()
elif parcelas == 0:
    limpar()
    print("Não possui parcelas à pagar")
    print(f"Preço final do carro: R${precoCarro * 0.80}")
else:
    limpar()
    print("Número de parcelas inválidas")
