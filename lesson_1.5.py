revenue = float(input('Выручка: '))
charge = float(input('Издержки: '))
profit = revenue - charge
rent = (profit / revenue * 100)

if revenue > charge:
    print(f"Прибыль = {profit:.2f}")
    print(f"Рентабильнасть =  {rent :.2f}%")
    people = float(input("Кол-во работников: "))
    pp = profit / people
    print(f"Прибыль фирмы в расчете на одного сотрудника = {pp}")


else:
    print('Фирма работает в УБЫТОК!!!')