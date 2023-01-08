def tapis(n):
    i = 0
    while i <= n:
        print("|", end=" ")
        j = 0
        while j <= n:
            if i + j == n:
                print("X", end=" ")
            else:
                print("-", end=" ")
            j += 1
        print("|")
        i += 1

tapis(10)
