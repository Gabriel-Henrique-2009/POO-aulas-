lista = []
for i in range(4):
    x = int(input())
    lista.append(x)
    if len(lista) == 4:
        lista.sort()
        print(lista[0])
        print(lista[3])
        print(f"isso é que é soma {lista[1] + lista[2]}")




