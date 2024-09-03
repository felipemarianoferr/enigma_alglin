from enigma_alglin import *
import os
from pathlib import Path


n = len(global_alphabet)

def main():

    user = input("Digite sua mensagem aqui: ")
    tupla = gerar_matrizes_de_permutacao(n)
    p,q = tupla[0], tupla[1]
    crip = encriptar_enigma(user, p, q)
    print(f'Mensagem encriptada: {crip}')
    decriptada = decriptar_enigma(crip, p, q)
    print()
    print(f'Mensagem decriptada: {decriptada}')

if __name__ == "__main__":
    main()