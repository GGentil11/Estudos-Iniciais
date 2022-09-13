import re 
password = input("Insira a sua senha: ")
flag = 0
vet_s = []
while True:   
    if (len(password)<8): 
        flag = -1
        break
    elif not re.search("[a-z]", password): 
        flag = -1
        break
    elif not re.search("[A-Z]", password): 
        flag = -1
        break
    elif not re.search("[0-9]", password): 
        flag = -1
        break
    elif not re.search("[_@$]", password): 
        flag = -1
        break
    elif re.search("\s", password): 
        flag = -1
        break
    else: 
        flag = 0
        print("Valid Password") 
        break
    while password in vet_s:
        
if flag ==-1: 
    print("Not a Valid Password")