a = float(input("Введите первую сторону 1 прямоугольника: "))
b = float(input("Введите вторую сторону 1 прямоугольника: "))
c = float(input("Введите первую сторону 2 прямоугольника: "))
d = float(input("Введите вторую сторону 2 прямоугольника: "))
if ((a > c) and (b > d)) or ((a > d) and (b > c)):
    print("можно уместить")
else:
    print("нельзя уместить")