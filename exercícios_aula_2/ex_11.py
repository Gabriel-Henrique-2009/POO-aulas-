def Diagonal(b, h):
    hipo = (b**2 + h**2)**(1/2)
    return hipo
    
x, y = int(input('base: ')), int(input('altura: '))
print(Diagonal(3, 4))