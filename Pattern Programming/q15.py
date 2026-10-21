n = 9
mid = n//2 + 1
for i in range(1, n+1):
    count = mid - i + 1 if i <= mid else i - mid + 1
    for j in range(1, count+1):
        print("*", end=" ")
    print()