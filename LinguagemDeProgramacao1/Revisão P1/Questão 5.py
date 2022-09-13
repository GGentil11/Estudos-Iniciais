import os
import time

def limpar():
    os.system ('cls')

def espacamento():
    print("\n\n\n\n\n")

lista_alunos = []
def nome():
    limpar()
    lista_alunos.append(input("Informe o nome do Aluno: ").capitalize())
    print("Aluno adicionado ao sistema!")
    time.sleep(2)
    menuPrincipal()

lista_nota = []
def nota():
    limpar()
    lista_nota.append(input("Informe a nota do Aluno: "))
    print("Nota adicionada ao sistema!")
    time.sleep(2)
    menuPrincipal()

def fichaAlunos():
    limpar()
    ficha = dict(zip(lista_alunos, lista_nota))
    print(ficha)
    
def menuPrincipal():
    limpar()
    print("1. Incluir aluno\n"
          "2. Incluir nota do aluno\n"
          "3. Lista Alunos e Notas\n"
          "4. Sair do programa")
    espacamento()
    opcao = int(input("Selecione a opção desejada: "))
    while opcao != 4:
        if opcao == 1:
            nome()
            break
        elif opcao == 2:
            nota()
            break
        elif opcao == 3:
            fichaAlunos()
            break
        else:
            limpar()
            print("Opção inexistente!")
            break

menuPrincipal()