def div_mod(n):
    x = n[0]
    y = n[1]
    output = []
    output.extend((x//y, x % y, divmod(x,y)))
    return output


values = input("Enter the Two Numbers: ").split()
values = list(map(int, values))
result = div_mod(values)
for item in result:
    print(item)