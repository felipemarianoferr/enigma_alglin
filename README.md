# enigma_alglin

# Projeto: criptografia com clone digital da máquina Enigma
## Produzido por Felipe M. Ferreira e Luise P. Bastos

Este projeto implementa um sistema de criptografia inspiurado na maquina Enigma, ultilizando matrizes de permutacao para encriptar a decriptar mensagens. O codigo esta escrito em Python e faz uso da biblioteca Numpy para operacoes com matrizes. O alfabeto global ultilizado para criptografia inclui letras maiusculas e minusculas do alfabeto, numeros, espacos, e caracteres acenturados comuns da lingua portuguesa. 

Como usar: Use a funcao gerar_matrizes_de_personagens(N) para gerar as matrizes de permutacao P e R. Estas serao ulilizadas tanto na encriptacao quanto na descricao. Chame a funcao encriptar_enigma(mensagem, P, Q) passando a mensagem e ser encriptada e as matrizes de permutacao geradas. A funcao retornara a mensagem encriptada. Para decsriptar uma mensagem, chame a funcao descriptar_enigma(mensagem_encriptada, P, Q) passando a mensagem encriptada e as mesmas matrizes de permutacao usadas na encriptacao. A funcao retornara a mensagem original. 

Atencao: A encriptacao e altamente dependente das matrizes de permutacao, portanto, diferentes execucoes de codigo com novas matrizes irao gerar mensagens encriptadas distintas para o mesmo texto original. 

Atencao: O algoritmo baseia-se em operacoes matriciais que sao sensiveis a ordem das multiplicacoes. Garantir a ultilizacao das matrizes P e Q geradas inicialmente e fundamental para que o processo de descriptacao funcione. 



