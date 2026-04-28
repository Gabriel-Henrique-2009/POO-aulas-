class Viagem:
    def __init__(self, dest, dist, lt):
        self.set_destino(dest)
        self.set_distancia(dist)
        self.set_litros(lt)

    def set_destino(self, d):
        self.__destino = d

    def set_distancia(self, d):
        if d >= 0: self.__distancia = d
        else: raise ValueError()

    def set_litros(self, l):
        if l >= 0: self.__litros = l
        else: raise ValueError()

    def get_destino(self):
        return self.__destino

    def get_distancia(self):
        return self.__distancia

    def get_litros(self):
        return self.__litros

    def consumo(self):
        return self.__distancia / self.__litros

    def __str__(self):
        return f"Destino é {self.__destino}. Tem a distancia de {self.__distancia} que gasta {self.__litros}"

class Pais:
    def __init__(self, n, p, a):
        self.set_nome(n)
        self.set_populacao(p)
        self.set_area(a)

    def set_nome(self, n):
        self.__nome = n

    def set_populacao(self, p):
        if p >= 0: self.__populacao = p
        else: raise ValueError()

    def set_area(self, a):
        if a >= 0: self.__area = a
        else: raise ValueError()

    def get_nome(self):
        return self.__nome

    def get_populacao(self):
        return self.__populacao

    def get_area(self):
        return self.__area

    def densidade(self):
        return self.__populacao / self.__area

    def __str__(self):
        return f"O país é {self.__nome}. Tem a população de {self.__populacao} que vive em {self.__area} km²"

 
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.viagem()
            if op == 2: UI.pais()

    @staticmethod
    def menu():
        print("1-Viagem, 2-País, 3-Fim")
        op = int(input("Informe uma opção: "))
        return op    

    @staticmethod
    def viagem():
        print("Cálculo da área do retangulo")
        dest = input("Informe o lugar: ")
        dist = float(input("Informe a distancia em km: "))
        lt = float(input("Informe os litros da gasosa: "))
        x = Viagem(dest, dist, lt)
        consumo = x.consumo()
        string = x.__str__
        print(f"Uma viagem com as seguintes características: {string}")
        print(f"Tem o consumo = {consumo:.2f}")

    def pais():
        print("Cálculo do frete")
        n = input("Informe o nome do país: ")
        p = float(input("Informe a população do país: "))
        a = float(input("Informe o valor da distância em kilometros: "))
        x = Pais(n, p, a)
        densidade = x.densidade()
        string = x.__str__
        print(f"Um País com as seguintes características: {string}")
        print(f"Tem a densidade demográfica de {densidade:.2f}")


UI.main()