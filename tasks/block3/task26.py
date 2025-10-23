n = int(input("Введите число n (в данном случае оно должно быть 564): "))

# Перебираем возможные цифры
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            if 100 * b + 10 * c + a == n:
                x = 100 * a + 10 * b + c
                print(f"Исходное число x: {x}")