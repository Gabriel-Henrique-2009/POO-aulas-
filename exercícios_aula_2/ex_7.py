frase = input("Digite uma frase: ")
palavras = frase.split()

for i in range(len(palavras)):
    resultado = " ".join(palavras[i:])
    print(resultado)