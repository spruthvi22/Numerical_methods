def f(x) :
    return (x**2-10)

def df(x) :
    return (2*x)

def main() :
    x,tol=0.1,0.001 # changed initial guess from 0 to 0.1 to make sure the method converges to a root
    while(abs(f(x))>tol) :
        x=x-f(x)/df(x)
    print('\nThe root is x =',x)

if __name__=="__main__" :
    main()
