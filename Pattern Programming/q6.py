n = 9
for i in range(1, n+1):
    for j in range(1, n+1):
        if i <= 2 or i >= n-1 or j <= 2 or j >= n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()