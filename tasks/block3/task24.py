for last_digit in range(10):
    hundreds_part = 237 - last_digit * 10
    if 0 <= hundreds_part <= 9:
        for x in range(100, 1000):
            if x % 10 == last_digit:
                if last_digit * 10 + (x // 100) == 237:
                    print(f"Число x: {x}")
                    break