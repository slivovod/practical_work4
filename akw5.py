f = int(input("Введите число: "))
s = 1
for i in range(1, f + 1):
    s *= i
print("Факториал данного числа: ", s)