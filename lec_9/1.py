def f(x):
    return(10 - (3*(x**2)))

area = 1/3 * (f(-1) + f(3) + 4*f(0) + 2*f(1) +4*f(2))
print(area)
