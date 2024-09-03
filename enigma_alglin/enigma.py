import numpy as np
from typing import Tuple
import string

# Definindo o alfabeto global
global_alphabet = {
    char: idx for idx, char in enumerate(
        string.ascii_lowercase + string.ascii_uppercase + string.digits + ' ' +
        'áàãâéêíóôõúçÁÀÃÂÉÊÍÓÔÕÚÇ'
    )
}

def gerar_matrizes_de_permutacao(N: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gera duas matrizes de permutação de tamanho N x N.
    """
    P = np.eye(N)
    R = np.eye(N)

    P = np.random.permutation(P)
    R = np.random.permutation(R)
    return (P, R)

def encriptar_enigma(mensagem: str,
                     P: np.ndarray,
                     Q: np.ndarray) -> str:
    
    # Usar o alfabeto global
    matriz_mensagem = np.zeros((len(global_alphabet), len(mensagem)), dtype=int)
    
    contador = 0  
    for letra in mensagem:
        matriz_mensagem[global_alphabet[letra]][contador] = 1
        contador += 1

    encriptador = P
    nova_mensagem = ''

    for i in range(matriz_mensagem.shape[1]):
        coluna = matriz_mensagem[:, i]
        if i == 0:
            coluna = encriptador @ coluna
        else:
            encriptador = Q @ encriptador
            coluna = encriptador @ coluna
        pos = np.where(coluna == 1)[0]
        for chave, valor in global_alphabet.items():
            if valor == pos:
                nova_mensagem += chave

        matriz_mensagem[:, i] = coluna

    return nova_mensagem

def decriptar_enigma(mensagem_encriptada: str,
                     P: np.ndarray,
                     Q: np.ndarray) -> str:
    
    matriz_mensagem_encriptada = np.zeros((len(global_alphabet), len(mensagem_encriptada)), dtype=int)

    contador = 0  
    for letra in mensagem_encriptada:
        matriz_mensagem_encriptada[global_alphabet[letra]][contador] = 1
        contador += 1

    decriptador = np.linalg.inv(P)
    nova_mensagem = ''

    for i in range(matriz_mensagem_encriptada.shape[1]):
        coluna = matriz_mensagem_encriptada[:, i]
        if i == 0:
            coluna = decriptador @ coluna
        else:
            decriptador = decriptador @ np.linalg.inv(Q)
            coluna = decriptador @ coluna
        pos = np.where(coluna == 1)[0]
        for chave, valor in global_alphabet.items():
            if valor == pos:
                nova_mensagem += chave

        matriz_mensagem_encriptada[:, i] = coluna

    return nova_mensagem

# Testando o código
tupla = gerar_matrizes_de_permutacao(len(global_alphabet))
mensagem_teste = 'mitó'
criptada = encriptar_enigma(mensagem_teste, tupla[0], tupla[1])
descriptada = decriptar_enigma(criptada, tupla[0], tupla[1])

print(f"Mensagem original: {mensagem_teste}")
print(f"Mensagem criptografada: {criptada}")
print(f"Mensagem descriptografada: {descriptada}")
