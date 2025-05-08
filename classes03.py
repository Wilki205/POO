from datetime import datetime

dias = ["segunda", "Terça", "Quarta", "quinta", "Sexta", "sábado", "domingo"]

x = datetime.now()

print(x.day)
print(x.month)
print(x.year)
print(x.weekday())

print(f'Hoje é dia {x.day} de {x.month} de {x.year} e hoje é {dias[x.weekday()]}')


