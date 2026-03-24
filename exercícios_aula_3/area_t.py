# b = float(input("Digite a base do triângulo "))
# h = float(input("Digite a altura do triângulo "))
# a = b * h / 2
# print(f"A área do triângulo é {a:.2f}")

# b = float(input("Digite a base do segundo triângulo "))
# h = float(input("Digite a altura do segundo triângulo "))
# a = b * h / 2
# print(f"A área do segundo triângulo é {a:.2f}")

class triangulo:
    def __init__(self):
        # Atributos da classe
        self.b = 0
        self.h = 0

    def calc_area(self):
        # Método
        return self.b * self.h / 2

x = triangulo()
print(x.b, x.h)
x.b = float(input("Digite a base do triângulo "))
x.h = float(input("Digite a altura do triângulo "))
print(x.b, x.h)
a = x.calc_area()
print(f"A área do triângulo é {a:.2f}")