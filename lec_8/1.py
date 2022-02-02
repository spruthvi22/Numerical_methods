def f(x):
    return(10 - x**2)

a = -2
b = 2
n = 100
integral = 0.5 * (f(a) + f(b))

for i in range(n-1):
    integral += f(-2+(i*(b-a)/n))

integral *= (b-a)/n
print(integral)
