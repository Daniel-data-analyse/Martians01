x = int(input("x compomemt of first vector: "))
y = int(input("y compomemt of first vector: "))
z = int(input("x component of second vector: "))
k = int(input("y component of second vector: "))

def ortogonal(x, y, z, k):
    multiply = x*z + z * k
    if multiply == 0:
        print("multiply =", multiply)
        print("They are perpendicular")
    elif x / z == y / k:
        print("slope of first vector =", y/x)
        print("slope of second vector =", k/z)
        print("They are parallel")
    else:
        print("Neither (not parallel and not perpendicular)")
ortogonal(x, y, z, k)