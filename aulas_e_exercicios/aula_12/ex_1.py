from datetime import datetime, timedelta

#x = timedelta(hours = 1, minutes = 38)
#print(x)

#aula = datetime(2026, 5, 19, 14, 30)
#print(aula)

#print(aula + x)

nasc = datetime.strptime(input("Informe a data do nascimento: "), "%d/%m/%Y") # terceira forma
hoje = datetime.now()
tempo_vida = hoje - nasc
print(tempo_vida)

ano = tempo_vida.days // 365
meses = tempo_vida.days % 365 // 30
dia = tempo_vida.days % 365 % 30

print(f"Você tem {tempo_vida} dias, que são: {ano}, {meses} e {dia} dias")
