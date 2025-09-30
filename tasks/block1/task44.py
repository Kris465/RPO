import math

a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))

perimeter = 2 * (a + b)

diagonal = math.sqrt(a ** 2 + b ** 2)

print(f"Периметр прямоугольника: {perimeter}")
print(f"Длина диагонали: {diagonal}")