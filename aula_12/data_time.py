from datetime import datetime

y = datetime(2026, 5, 19, 14, 30, 0) # primeira forma
print(y)
print(y.day)
print(y.month)
print(y.year)
print(y.hour)
print(y.minute)
print(y.second)
print(y.date)
print(y.time)
print(y.weekday)

z = datetime.now() # segunda forma
print(z)
print(z.strftime("%d/%m/%Y , %H:%M:%S"))
print(z.strftime("%d/%m/%y"))
print(z.strftime("%d/%m/%a")) 

x = datetime.strptime(input("Informe uma data: "), "%d/%m/%Y") # terceira forma
print(x)
print(x.strftime("%d/%m/%Y"))