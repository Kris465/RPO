n = int(input("Введите число n (100 ≤ n ≤ 999): "))

for x in range(100, 1000):
    a = x // 100
    b = (x // 10) % 10
    c = x % 10

    two_digit = 10 * a + c

    n_candidate = two_digit * 10 + b

    if n_candidate == n:
        print(f"Исходное число x: {x}")
        break
else:
    print("Не найдено подходящего числа.")
