X = int(input("Введите первое число: "))
Y = int(input("Введите второе число: "))
Z = int(input("Введите третье число: "))

primer_one = (X % 2 == 1) and (Y % 2 == 1)
primer_two = (X < 20) or (Y < 20)
primer_three = (X == 0) or (Y == 0)
primer_four = (X < 0) and (Y < 0) and (Z < 0)
primer_five = (X % 5 == 0) or (Y % 5 == 0) or (Z % 5 == 0)
primer_six = (X > 100) or (Y > 100) or (Z > 100)

print(f"a) {primer_one}")
print(f"б) {primer_two}")
print(f"в) {primer_three}")
print(f"г) {primer_four}")
print(f"д) {primer_five}")
print(f"е) {primer_six}")
