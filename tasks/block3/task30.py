for a in range(1, 10):
    for c in range(0, 10):
        b = 456 - 100 * a - 10 * c
        if 0 <= b <= 9:
            x = a * 100 + b * 10 + c
            print(f"Найдено число x: {x}")