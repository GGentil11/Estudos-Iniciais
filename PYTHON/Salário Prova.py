saldo = float(input("Informe o saldo médio: "))

if saldo <= 2000:
    novoSaldo = saldo * 1.10
    credito = novoSaldo - saldo
elif saldo > 2000 and saldo <= 3000:
    novoSaldo = saldo * 1.20
    credito = novoSaldo - saldo 
elif saldo > 3000 and saldo <= 4000:
    novoSaldo = saldo * 1.25
    credito = novoSaldo - saldo 
else: saldo > 4000
novoSaldo = saldo * 1.30
credito = novoSaldo - saldo

print("Saldo médio: {}" .format(novoSaldo))
print("Valor do crédito: {}" .format(credito))