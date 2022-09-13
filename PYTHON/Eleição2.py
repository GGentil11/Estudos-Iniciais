from array import array
from itertools import count
from operator import index
import os
from random import Random, random
import time, sys
import pandas


def limpar():
    os.system('cls')

votosJoao = 0
votosMaria = 0
votosFrancisco = 0
votosRaimunda = 0
votosNulos = 0
votosBranco = 0

numero = 0

while numero!=999:
    limpar()
    print("--Escolha o seu candidato--",
    "\nCandidato João: 10",
    "\nCandidata Maria: 20",
    "\nCandidato Francisco: 30",
    "\nCandidata Raimunda: 40",
    "\nVoto Nulo: 98",
    "\nVoto em Branco: 99",
    "\nUse código 999 para encerrar a votação geral")

    numero = int(input("\nInsira o número do seu candidato:"))

    if numero == 10:
        votosJoao += 1
    elif numero == 20:
        votosMaria += 1
    elif numero == 30:
        votosFrancisco += 1
    elif numero == 40:
        votosRaimunda += 1
    elif numero == 98:
        votosNulos += 1
    elif numero == 99:
        votosBranco += 1
    elif numero == 999:
        limpar()
        print("Votação encerrada!", "\nGerando resultados...")
        time.sleep (2)
    else:
        print("Informe um número válido!")
        time.sleep (2)

votosTotal = votosJoao + votosMaria + votosFrancisco + votosRaimunda + votosNulos + votosBranco
if votosTotal > 0:
    percNulos = votosNulos * 100.0 / votosTotal
    percBranco = votosBranco * 100.0 / votosTotal
    percJoao = votosJoao * 100.0 / votosTotal
    percMaria = votosMaria * 100.0 / votosTotal
    percFrancisco = votosFrancisco * 100.0 / votosTotal
    percRaimunda = votosRaimunda * 100.0 / votosTotal

    limpar()
    print(f"Foram contabilzados {votosTotal} votos\n")  
    print(f"João recebeu {votosJoao} votos | Representando {round(percJoao, 2)}% dos votos totais")
    print(f"Maria recebeu {votosMaria} votos | Representando {round(percMaria, 2)}% dos votos totais")
    print(f"Francisco recebeu {votosFrancisco} votos | Representando {round(percFrancisco, 2)}% dos votos totais")
    print(f"Raimunda recebeu {votosRaimunda} votos | Representando {round(percRaimunda, 2)}% dos votos totais")
    print(f"Foram contabilizados {votosNulos} votos nulos | Representando {round(percNulos, 2)}% dos votos totais")
    print(f"Foram contabilizados {votosBranco} votos em branco | Representando {round(percBranco, 2)}% dos votos totais")
  
    
    

    listVotos = [votosJoao, votosMaria, votosFrancisco, votosRaimunda]
    listVotos.sort()
    vencedor = max(listVotos)
    
    if vencedor == votosJoao:
        print(f"O candidato João foi eleito com {vencedor} votos")
    elif vencedor == votosMaria:
        print(f"A candidata Maria foi eleita com {vencedor} votos")
    elif vencedor == votosFrancisco:
        print(f"O candidato Francisco foi eleito com {vencedor} votos")
    elif vencedor == votosRaimunda:
        print(f"A candidata Raimunda foi eleita com {vencedor} votos")
  