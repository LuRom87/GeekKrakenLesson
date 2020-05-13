a = float(input("Введите первое число: "))
z = input("Введите действие: ")
b = float(input("Введите второе число: "))

if z == "+":
    print(a + b)
elif z == "-":
    print(a - b)
elif z == "*":
    print(a * b)
elif z == "/":
    print(a / b)
elif z != "+, -, *, /":
    print("Вы ввели не правильное действие!!!!")
