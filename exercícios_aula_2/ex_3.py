lista = []
for i in range(4):
    x = int(input())
    lista.append(x)
    if len(lista) == 4:
        if len(set(lista)) != 4:
            # ele consegue verificar todos os valores dentro de uma lista. Ideal para remover duplicatas
            print("coisas erradas estão acontecendo")
        else:
            lista.sort()
            print(f"O maior item da lista é {lista[3]}")
            print(f"O menor item da lista é {lista[0]}")
            print(f"isso é que é soma {lista[1] + lista[2]}")

