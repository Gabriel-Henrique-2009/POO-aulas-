lista = []
for i in range(3):
    x = int(input())
    lista.append(x)

menor = min(lista)
maior = max(lista)
meio = sum(lista) - menor - maior

print(f"{menor}, {meio}, {maior}")
