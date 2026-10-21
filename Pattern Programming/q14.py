n=7
mid = n//2 + 1
for i in range(1, n+1):
    count = i if i <= mid else n - i + 1
    for j in range(1, count+1):
        print("*", end=" ")
    print()