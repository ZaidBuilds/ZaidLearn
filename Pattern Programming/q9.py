n = 7
mid = n//2 + 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == mid or j == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()