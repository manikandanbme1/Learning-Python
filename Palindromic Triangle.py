def palindromictriangle(n):
    for i in range(1, n + 1):
        print(int((10**i-1) / 9) ** 2)


palindromictriangle(int(input("Enter the Number: ")))