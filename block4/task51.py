a = int(input("Введите сторону а: "))
b = int(input("Введите сторону b: "))
c = int(input("Введите сторону c: "))
d = int(input("Введите сторону d: "))


if (a + 1 <= c and b + 1 <= d) or (a + 1 <= d and b + 1 <= c):
    print(f'Письмо {a} {b} может уместиться внутри конверта {c} и {d}')
else:
    print(f'Письмо {a} {b} не может уместиться внутри конверта {c} и {d}')
