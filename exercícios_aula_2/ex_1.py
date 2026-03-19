a = int(input())
b = int(input())
c = int(input())
d = int(input())

par = 0
impar = 0

if a % 2 == 0: par += a
else: impar += a
if b % 2 == 0: par += b
else: impar += b
if c % 2 == 0: par += c
else: impar += c
if d % 2 == 0: par += d
else: impar += d

print(f"A soma de numeros pares é de {par}")
print(f"A soma de numeros impares é de {impar}")