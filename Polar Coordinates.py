import cmath

user = complex(input("Enter a Complex number: "))


def polar_coordinates(cp):
    output = []
    phase = cmath.phase(cp)
    magn = abs(cp)
    output.extend((magn, phase))
    return output


result = polar_coordinates(user)
for item in result:
    print(item)



