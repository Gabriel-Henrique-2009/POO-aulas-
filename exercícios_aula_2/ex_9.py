frase = input("Digite uma frase: ")
palavras = frase.split()

for p in palavras:
    palavra_invertida = p[::-1]
    print(palavra_invertida)