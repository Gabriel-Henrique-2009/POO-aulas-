class maior:
    def __init__(self, a, b):
        self.valor_a = a
        self.valor_b = b    

    def calc(self):
        if self.valor_a == self.valor_b:
            return "valor igual"
        else:
            return max(self.valor_a, self.valor_b)
            

m = maior(int(input()), int(input()))  
print(m.calc()) 
 
o = maior(int(input()), int(input()))  
print(o.calc())  