from enigma_alglin import *
import os
from pathlib import Path


t = {}

def main():

    user = input("Digite sua mensagem aqui: ")
    n = len(tabela(user))
    tupla = gerar_matrizes_de_permutacao(n)
    p,q = tupla[0], tupla[1]
    crip = encriptar_enigma(user, p, q)
    print(crip)
    print(decriptar_enigma(crip, p, q))

if __name__ == "__main__":
    main()