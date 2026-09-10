import math
class circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * (self.raio**2)
    
    def circunferencia(self):
        return 2* math.pi * self.raio

c = circulo(5)
print(c.area())
print(c.circunferencia())