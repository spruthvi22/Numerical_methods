from scipy import interpolate as intp

def main() :
    x,y=[0,1,2],[1,2,4]
    interpolated=intp.CubicSpline(x,y)
    print('The interpolated value of f(1.5) is ',interpolated(1.5))
    print('The analytical value of f(1.5) is',2**(1.5))

if __name__=="__main__" :
    main()
