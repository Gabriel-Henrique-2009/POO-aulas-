lista = []
for i in range(4):
    x = int(input())
    lista.append(x)
    if len(lista) == 4:
        if lista[0] == lista[1] or lista[2] == lista[3] or lista[1] == lista[2] or lista[1] == lista[3] or lista[2] == lista[3]:
            print("coisas erradas estão acontecendo")
        else:
            lista.sort()
            print(lista[0])
            print(lista[3])
            print(f"isso é que é soma {lista[1] + lista[2]}")
            print