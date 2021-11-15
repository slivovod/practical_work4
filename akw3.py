a = input()
b = input()
c = input()

if(a + b > c and a + c > b and b + c > a):
    print("Такой треугольник существует")
else:
    print("Такого треугольника не существует")