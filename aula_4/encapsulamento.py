# O encapsulamento serve para que o valor de uma class não seja alterado facilmente, que evita alguns erros na produção do códigoem python. Veja alguns exemplos:
class retangulo:
    def __init__(self):
        self.__base = 0
        self.__altura = 0

    def set_base(self, valor):
        if valor < 0: raise ValueError("O valor seve ser positivo")
        self.__base = valor

    def get_base(self):
        return self.__base

    def set_altura(self, valor):
        if valor < 0: raise ValueError("O valor seve ser positivo")
        self.__altura = valor

    def get_altura (self):
        return self.__altura
        
    def diagonal (self):
        return (self.__base ** 2 + self.__altura ** 2) ** 0.5

class chamamento:
    def main():
        x = retangulo()
        x.set_base(float(input("Base: ")))
        x.set_altura(float(input("Altura: ")))
        diagonal = x.diagonal()
        print(diagonal)

chamamento.main()
        