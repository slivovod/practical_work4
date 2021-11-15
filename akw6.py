sq = int(input())
for i in range(sq):
    for j in range(sq + 1):
        if(i < j  <= sq - i or sq - i <= j <= i + 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()