print("Digite uma data no formato dd/mm/aaaa")
data = int(input("data"))
mes = int(input("mês"))
ano = int(input("Ano"))

data_invalida = False

if not(1900 <= ano <= 2100):
    data_invalida = True

if not(1 <= mes <= 12):
    data_invalida = True

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 9 or mes == 11:
    if not(1 <= data <= 31):
        data_invalida = True

if mes == 4 or mes == 6 or mes == 8 or mes == 10 or mes == 12:
    if not(1 <= data <= 30):
        data_invalida = True

if mes == 2:
    if not(1 <= data <= 28):
        data_invalida = True

if data_invalida == False:
    print("Sua data é válida")
else:
    print("Sua data é inválida")