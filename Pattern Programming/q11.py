n = 7
mid = n//2 + 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == mid or j == mid or j == 1 and i < mid or j == n and i > mid or i == 1 and j > mid or i == n and j < mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()