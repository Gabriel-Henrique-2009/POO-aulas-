class triangulo:
    def __init__(self):
        # Atributos da classe
        self.b = 0
        self.h = 0

    def calc_area(self):
        # Método é o init
        return self.b * self.h / 2

x = triangulo()
print(x.b, x.h)
# acessa os valores que estão dentro da classe x (triangulo)

x.b = float(input("Digite a base do triângulo "))
x.h = float(input("Digite a altura do triângulo "))

print(x.b, x.h)

a = x.calc_area()
print(f"A área do triângulo é {a:.2f}")

y = triangulo()
print(y.b, y.h)

y.b = float(input("Digite a base do triângulo "))
y.h = float(input("Digite a altura do triângulo "))

print(y.b, y.h)

a = y.calc_area()
print(f"A área do triângulo é {a:.2f}")

