def soma(frase):
    soma = 0
    for c in frase:
        if c.isdigit():
            soma += int(c)
    return soma

print(soma(input("Digite uma frase: ")))
