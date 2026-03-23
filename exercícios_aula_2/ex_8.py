frase = input("Digite uma frase: ")
rotacao = frase

for _ in range(len(frase)):
    rotacao = rotacao[1:] + rotacao[0]
    print(rotacao)