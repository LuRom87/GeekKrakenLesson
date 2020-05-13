
time = int(input('Введите время в секундах: '))

hours = time // 3600
min = (time - hours * 3600) // 60
sec = time % 3600 % 60
print(f"{hours:02d}:{min:02d}:{sec:02d}")
