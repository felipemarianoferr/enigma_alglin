import numpy as np
from typing import Tuple
import copy

def gerar_matrizes_de_permutacao(N : int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gera duas matrizes de permutação de tamanho N x N.
    """

    P = np.eye(N)
    R = np.eye(N)

    P = np.random.permutation(P)
    R = np.random.permutation(R)
    return (P,R)

def tabela(mensagem):

    mensagem = np.unique(list(mensagem))
    tabela = {}
    contador = 0
    for letra in mensagem:
        if letra not in tabela:
            tabela[str(letra)] = contador
            contador += 1

    return tabela

def encriptar_enigma(mensagem : str,
              P : np.ndarray,
              Q : np.ndarray) -> str:
    
    global t
    t = tabela(mensagem)
    
    matriz_mensagem = np.zeros((len(t), len(mensagem)), dtype=int)
    
    contador = 0  
    for letra in mensagem:
        matriz_mensagem[t[letra]][contador] = 1
        contador += 1

    encriptador = P
    nova_mensagem = ''
    #print(f"antes: {matriz_mensagem}")

    for i in range(matriz_mensagem.shape[1]):
        coluna = matriz_mensagem[:,i]
        if i == 0:
            coluna = encriptador@coluna
        else:
            encriptador = Q @ encriptador
            coluna = encriptador@coluna
        pos = np.where(coluna == 1)[0]
        for chave, valor in t.items():
            if valor == pos:
                nova_mensagem += chave

        matriz_mensagem[:, i] = coluna

    #print(f"depois: {matriz_mensagem}")

    return nova_mensagem
                

def decriptar_enigma(mensagem_encriptada : str,
              P : np.ndarray,
              Q : np.ndarray) -> str:
    
    matriz_mensagem_encriptada = np.zeros((len(t), len(mensagem_encriptada)), dtype=int)

    contador = 0  
    for letra in mensagem_encriptada:
        matriz_mensagem_encriptada[t[letra]][contador] = 1
        contador += 1


    decriptador = np.linalg.inv(P)
    nova_mensagem = ''

    for i in range(matriz_mensagem_encriptada.shape[1]):
        coluna = matriz_mensagem_encriptada[:,i]
        if i == 0:
            coluna = decriptador@coluna
        else:
            decriptador = decriptador @ np.linalg.inv(Q) 
            coluna = decriptador@coluna
        pos = np.where(coluna == 1)[0]
        for chave, valor in t.items():
            if valor == pos:
                nova_mensagem += chave

        matriz_mensagem_encriptada[:, i] = coluna

    return nova_mensagem

# tupla = gerar_matrizes_de_permutacao(3)
# criptada = encriptar_enigma('aabbcc', tupla[0], tupla[1])
# print(criptada)
# print(decriptar_enigma(criptada, tupla[0], tupla[1]))
