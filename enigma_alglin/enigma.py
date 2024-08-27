import numpy as np
from typing import Tuple

def gerar_matrizes_de_permutacao(N : int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gera duas matrizes de permutação de tamanho N x N.
    """
    raise NotImplementedError

def encriptar_enigma(mensagem : str,
              P : np.ndarray,
              Q : np.ndarray) -> str:
    raise NotImplementedError

def decriptar_enigma(mensagem_encriptada : str,
              P : np.ndarray,
              Q : np.ndarray) -> str:
    raise NotImplementedError
