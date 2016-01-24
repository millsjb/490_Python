def sqroot_newton(a):
    x = a/2
    y = ((x)+(a/x)/2)
    while abs(y - x) >= 0.005:
        y = (sqroot_newton(x)+a/sqroot_newton(x))/2
    return y



def sqrt(a):
    x = a/2
    y = ((sqrt(x))+(a/sqrt(x))/2)
    if abs(y - x) <= 0.005:
        return y

print(sqrt(11))
