n = 4
try:
    n = int(input("Введите количество чисел(def = 4): "))
    if(n == 0):
        n = 4
        print("Количество чисел - 4")
except:
    print("Количество чисел - 4")

arr = []
for i in range(0, n):
    s = int(input())
    arr.append(s)

mx = arr[1]
for i in range(0, n):
    if(arr[i] > mx):
        mx = arr[i]

print(mx)