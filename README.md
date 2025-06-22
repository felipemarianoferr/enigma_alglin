# enigma_alglin

# Project: encryption with a digital clone of the Enigma machine  
## Produced by Felipe M. Ferreira and Luise P. Bastos

This project implements an encryption system inspired by the Enigma machine, using permutation matrices to encrypt and decrypt messages. The code is written in Python and uses the NumPy library for matrix operations. The global alphabet used for encryption includes uppercase and lowercase letters, numbers, spaces, and common accented characters of the Portuguese language.

How to use: Use the function `gerar_matrizes_de_personagens(N)` to generate the permutation matrices `P` and `R`. These will be used both for encryption and decryption. Call the function `encriptar_enigma(message, P, Q)` passing the message to be encrypted and the generated permutation matrices. The function will return the encrypted message. To decrypt a message, call the function `descriptar_enigma(encrypted_message, P, Q)` passing the encrypted message and the same permutation matrices used for encryption. The function will return the original message.

Attention: Encryption is highly dependent on the permutation matrices; therefore, different code executions with new matrices will generate distinct encrypted messages for the same original text.

Attention: The algorithm is based on matrix operations that are sensitive to the order of multiplications. Ensuring the use of the initially generated `P` and `Q` matrices is fundamental for the decryption process to work.
