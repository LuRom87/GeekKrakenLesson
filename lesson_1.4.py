n = int(input("Введите целое положительное число "))
z = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > z:
        z = n % 10
    else:
        print("Самая большая цифра в числе ", z)
        break