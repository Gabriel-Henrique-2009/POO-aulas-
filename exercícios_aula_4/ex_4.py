def soma(lista):
    soma = 0
    for c in lista:
        if c.isdigit():
            soma += int(c)
    return soma

print(soma(input("Digite uma lista de numeros: ")))