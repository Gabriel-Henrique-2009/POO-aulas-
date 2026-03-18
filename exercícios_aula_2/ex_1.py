par = 0
impar = 0
for i in range(4):
    x = int(input())
    if x % 2 == 0:
        par += x
    else:
        impar += x

print(f"a soma dos pares é {par}")
print(f"a soma dos impares é {impar}")