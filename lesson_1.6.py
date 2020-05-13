a = int(input("Первый день: "))
b = int(input("Последний день: "))
days = 1
km = a
while a < b:
    a = a + a * 10 / 100
    days += 1
    km = km + a
print(f"Спортсмен достиг результата на %.d день" % days)