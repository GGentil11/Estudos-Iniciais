import re
password_list = list(password = [])
password = input("Informe a sua senha: ")
erro = 0
if len (password) < 6 :
    erro += 1
elif not re.search (["A"-"Z"], password):
    erro += 1
elif not re.search (["0"-"9"], password):
    erro += 1
elif