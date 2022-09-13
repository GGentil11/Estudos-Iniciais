qtdProduto = 0
c = 0
coisas = []

for c in range(5):
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite agora o preço: '))
    
    
if preco < 50:
    qtdProduto += 1
elif preco > 50 and preco < 100:
    print
