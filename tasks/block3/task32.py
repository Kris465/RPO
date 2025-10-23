x_found = None

# Перебираем возможные цифры a, b, c
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            if 100 * c + 10 * b + a == 654:
                # Итак, исходное число:
                x = 100 * a + 10 * b + c
                x_found = x
                break
        if x_found is not None:
            break
    if x_found is not None:
        break

if x_found is not None:
    print(f"Найденное число x: {x_found}")
else:
    print("Соответствий не найдено.")