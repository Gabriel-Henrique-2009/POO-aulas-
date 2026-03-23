def MenorInteiro(x):
    int_x = int(x)
    if x <= int_x:
        return int_x
    else:
        return int_x + 1

a = float(input('escreva o número: '))
print(MenorInteiro(a))

