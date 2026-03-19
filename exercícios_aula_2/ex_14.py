def RemoverEspacos(texto):
    recorte = texto.split()
    frase = "".join(recorte)
    texto = frase[::1]
    return texto

a = input('escreva aqui: ')
print(RemoverEspacos(a))