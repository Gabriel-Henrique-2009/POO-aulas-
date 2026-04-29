class Retangulo:
    def __init__(self, h, b):
        self.set_base(b)
        self.set_altura(h)
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError("Base não pode ser negativa")
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError("Altura não pode ser negativa")
    def get_base(self): return self.__b
    def get_altura(self): return self.__h
    def calc_area(self): return self.__b * self.__h
    def calc_diagonal(self): return (self.__b ** 2 + self.__h ** 2) ** 0.5
    def __str__(self): return f"Base = {self.__b} - Altura = {self.__h}"

class Frete:
    def __init__(self, p, d):
        self.set_peso(p)
        self.set_distancia(d)
    def set_peso(self, v):
        if v >= 0: self.__p = v
        else: raise ValueError("Peso não pode ser negativo")
    def set_distancia(self, v):
        if v >= 0: self.__d = v
        else: raise ValueError("Distância não pode ser negativa")
    def calc_frete(self): return (0.01 * self.__p) * self.__d
    def __str__(self): return f"Peso = {self.__p}kg - Distância = {self.__d}km"

class Equa_segundo_grau:
    def __init__(self, a, b, c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

    def set_a(self, v):
        if v != 0: self.__a = v
        else: raise ValueError("O coeficiente 'a' não pode ser zero.")
    def set_b(self, v): self.__b = v
    def set_c(self, v): self.__c = v

    def delta(self):
        return self.__b ** 2 - 4 * self.__a * self.__c

    def tem_raiz_real(self):
        if self.delta() >= 0: return True
        else: return False

    def raiz1(self):
        if not self.tem_raiz_real(): return None
        return (-self.__b + self.delta() ** 0.5) / (2 * self.__a)

    def raiz2(self):
        if not self.tem_raiz_real(): return None
        return (-self.__b - self.delta() ** 0.5) / (2 * self.__a)

    def __str__(self):
        return f"{self.__a}x² + {self.__b}x + {self.__c} = 0"

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = UI.menu()
            if op == 1: UI.retangulo()
            elif op == 2: UI.frete()
            elif op == 3: UI.equacao()

    @staticmethod
    def menu():
        print("\n1-Retângulo, 2-Frete, 3-Equação, 4-Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def retangulo():
        h = float(input("Base: "))
        b = float(input("Altura: "))
        obj = Retangulo(h, b)
        print(f"{obj}")
        print(f"Área: {obj.calc_area():.2f} | Diagonal: {obj.calc_diagonal():.2f}")

    @staticmethod
    def frete():
        p = float(input("Peso (kg): "))
        d = float(input("Distância (km): "))
        obj = Frete(p, d)
        print(f"{obj}")
        print(f"Valor do Frete: R$ {obj.calc_frete():.2f}")

    @staticmethod
    def equacao():
        a = float(input("Valor de a: "))
        b = float(input("Valor de b: "))
        c = float(input("Valor de c: "))
        eq = Equa_segundo_grau(a, b, c)
        d = eq.delta()
        print(f"Equação: {eq}")
        print(f"Delta: {d}")
        if eq.tem_raiz_real() == True:
            print("Raizes reais: True")
            print(f"Raiz 1: {eq.raiz1():.2f}")
            print(f"Raiz 2: {eq.raiz2():.2f}")
        else:
            print("Possui raízes reais: False")

UI.main()