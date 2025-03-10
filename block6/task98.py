def calculate_deposit():
    initial_amount = 1000
    monthly_interest = 0.02
    month = 0

    month_increase_exceeds_30 = None
    month_amount_exceeds_1200 = None

    current_amount = initial_amount

    while True:
        month += 1
        increase = current_amount * monthly_interest
        current_amount += increase

        if month_increase_exceeds_30 is None and increase > 30:
            month_increase_exceeds_30 = month

        if month_amount_exceeds_1200 is None and current_amount > 1200:
            month_amount_exceeds_1200 = month

        if month_increase_exceeds_30 is not None and month_amount_exceeds_1200\
        is not None:
            break

    return month_increase_exceeds_30, month_amount_exceeds_1200

month_increase, month_amount = calculate_deposit()
print(f"а) Величина ежемесячного увеличения вклада превысит 30 руб. на {month_increase} месяце.")
print(f"б) Размер вклада превысит 1200 руб. через {month_amount} месяцев.")
