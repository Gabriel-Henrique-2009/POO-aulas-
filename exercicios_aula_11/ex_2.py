a = int(input("idade 1: "))
b = int(input("idade 2: "))
c = int(input("idade 3: "))
lista = [a, b, c]
min = min(lista)
max = max(lista)
print(sum(lista) - min - max)