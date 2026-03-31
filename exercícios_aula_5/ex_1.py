class agua:
    def __init__(self, ano, mes, consumo_m):
        self.ano= ano
        self.mes = mes
        self.cons = consumo_m

    def func_preco(self):     
        if self.cons <= 10:
            preco = 38

        elif 11 <= self.cons <= 20:
            preco = 38 + (self.cons - 10) * 5
        
        elif self.cons >=21:
            preco = 88 + (self.cons - 20) * 6
        
        print(f"o mês é {self.mes} do ano {self.ano} e sua continha foi de {preco} reais")
        
        
d = agua(int(input("digite o ano: ")), int(input("digite o mes: ")), int(input("digite o consumo por metro cúbico: ")))
d.func_preco()

 