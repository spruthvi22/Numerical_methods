def main() :
    x,y=[0,1,2],[1,2,4]
    L=[1,1,1]
    x0,y0=1.5,0

    for i in range(3) :
        for j in range(3) :
            if i==j : continue
            L[i]*=(x0-x[j])/(x[i]-x[j])

    for i in range(3) : y0+=y[i]*L[i]
    print("f(1.5) =",y0)

if __name__=="__main__" :
    main()

