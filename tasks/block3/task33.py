n = int(input("Введите число n (1 ≤ n ≤ 999), цифра единиц в n не равна нулю: "))

# Проверка, что последняя цифра n != 0
if n % 10 == 0:
    print("Ошибка: цифра единиц числа n не должна быть нулем.")
else:
    x_found = None
    for a in range(1, 10):
        for b in range(0, 10):
            for c in range(1, 10):
                # Проверка условия
                if 100 * c + 10 * b + a == n:
                    # Нашли подходящее x
                    x = 100 * a + 10 * b + c
                    x_found = x
                    break
            if x_found is not None:
                break
        if x_found is not None:
            break

    if x_found is not None:
        print(f"Исходное число x: {x_found}")
    else:
        print("Соответствия не найдено.")