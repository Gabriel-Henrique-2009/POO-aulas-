from this import d


class Retangulo:
    def __init__(self, h, b):
        self.set_base(b)
        self.set_altura(h)
    def set_base(self, v):
        if v >=0 : self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h
    def calc_diagonal(self):
        return (self.__b ** 2 + self.__h ** 2) ** 0.5
    def __str__(self):
        return f"Base = {self.__b} - Altura = {self.__h}"

class Frete:
    def __init__(self, p, d):
        self.set_peso(p)
        self.set_distancia(d)
    def set_peso(self, v):
        if v >=0 : self.__p = v
        else: raise ValueError()
    def set_distancia(self, v):
        if v >= 0: self.__d = v
        else: raise ValueError()
    def get_peso(self):
        return self.__p
    def get_distancia(self):
        return self.__d
    def calc_frete(self):
        return (0.01 * self.__p) * self.__d
    def __str__(self):
        return f"Peso (em kg) = {self.__p} - distancia (em km) = {self.__d}"

class Equa_segundo_grau:
    def __init__(self, a, b, c, x):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)
        self.set_x(x)

    def set_a(self, v):
        if v > 0 or v < 0 : self.__a = v
        else: raise ValueError()

    def set_b(self, v):
        if v >= 0 or v < 0: self.__b = v

    def set_c(self, v):
        if v >= 0 or v < 0: self.__c = v

    def set_x(self, v):
        if v >= 0 or v < 0: self.__x = v


    def delta(self):
        return self.__b ** 2 - 4 * self.__a * self.__c

    def tem_raiz_real(self):
        raiz_real = True
        delta = Equa_segundo_grau.delta
        if delta < 0: raiz_real = False
        return raiz_real

    def raiz1(self):
        delta = Equa_segundo_grau.delta
        return ((-1 * self.__b) + delta ** 0.5) / 4 * self.__a

    def raiz2(self):
        delta = Equa_segundo_grau.delta
        return ((-1 * self.__b) - delta ** 0.5) / 4 * self.__a

    def __str__(self):
        return f"a = {self.__a}, b = {self.__b}, c = {self.__c} e x = {self.__x}"
    
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.retangulo()
            if op == 2: UI.frete()
            if op == 3: UI.equacao()

    @staticmethod
    def menu():
        print("1-Retângulo, 2-Frete, 3-Equação do segundo grau e 4-Fim")
        op = int(input("Informe uma opção: "))
        return op    

    @staticmethod
    def retangulo():
        print("Cálculo da área do retangulo")
        h = float(input("Informe o valor da base: "))
        b = float(input("Informe o valor da altura: "))
        x = Retangulo(h, b)
        area = x.calc_area()
        diagonal = x.calc_diagonal()
        print(f"Um retângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area:.2f} e tem diagonal = {diagonal:.2f}")

    def frete():
        print("Cálculo do frete")
        p = float(input("Informe o valor do peso em kilos: "))
        d = float(input("Informe o valor da distância em kilometros: "))
        x = Frete(p, d)
        frete = x.calc_frete()
        print(f"Uma viagem de {x.get_distancia()} km's e trasportando o peso de {x.get_peso()} tem o frete = {frete:.2f} reais")

    def equacao():
        print("Cálculo do frete")
        a = float(input("Valor de a: "))
        b = float(input("Valor de b: "))
        c = float(input("Valor de c: "))
        x = float(input("Valor de x: "))
        x = Equa_segundo_grau(a, b, c, x)
        frete = x.calc_frete()
        frete = x.calc_frete()
        frete = x.calc_frete()
        frete = x.calc_frete()
        print(f"Uma viagem de {x.get_distancia()} km's e trasportando o peso de {x.get_peso()} tem o frete = {frete:.2f} reais")
UI.main()