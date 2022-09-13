nome = input("Informe o seu nome: ")

sexo = input("Informe o seu sexo (m ou f): ").strip().upper()

if sexo == 'M':
    print("Seja bem-vindo ,{}". format(nome))
elif sexo == 'F':
    print("Seja bem-vinda ,{}". format(nome))
else:
    print("Ocorreu um erro!")