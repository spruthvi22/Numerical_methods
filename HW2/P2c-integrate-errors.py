# Problem 2 (c). : Plotting I_i-I_{i-1} for left-point, mid-point, right-point, trapezoidal and Simpson's rules.

import numpy as np
import matplotlib.pyplot as plt

def f(x) :
    return np.exp(x)

def left_point(N) :
    dx,I=1/N,0.0
    x=np.linspace(0,1-dx,N)
    for i in range(N) :
        I+=dx*f(x[i])
    return I

def right_point(N) :
    dx,I=1/N,0.0
    x=np.linspace(dx,1,N)
    for i in range(N) : I+=dx*f(x[i])
    return I

def mid_point(N) :
    dx,I=1/N,0.0
    x=np.linspace(dx,1-dx/2,N)
    for i in range(N) :
        I+=dx*f(x[i])
    return I

def trapezoidal(N) :
    dx,I=1/N,0.0
    x=np.linspace(0,1,N)
    for i in range(1,N-1) : I+=f(x[i])
    I=dx*(I+f(x[0])/2+f(x[-1])/2)
    return I

def simpson(N) :
    dx,I=1/N,0.0
    x=np.linspace(0,1,N)
    for i in range(1,N-1) :
        if i%2==0 : I+=2*f(x[i])
        else : I+=4*f(x[i])
    I=(dx/3)*(I+f(x[0])+f(x[-1]))
    return I

def main() :
    left_errors,right_errors,mid_errors,trap_errors,simp_errors,lprev,rprev,mprev,tprev,sprev=[],[],[],[],[],0,0,0,0,0

    for i in range(1,15) :
        left_I=left_point(i)
        right_I=right_point(i)
        mid_I=mid_point(i)
        trap_I=trapezoidal(i)
        simp_I=simpson(i)
    
        left_errors.append(left_I-lprev)
        right_errors.append(right_I-rprev)
        mid_errors.append(mid_I-mprev)
        trap_errors.append(trap_I-tprev)
        simp_errors.append(simp_I-sprev)
        
        lprev=left_I
        rprev=right_I
        mprev=mid_I
        tprev=trap_I
        sprev=simp_I
    
    plt.plot(left_errors,label='Error in Left-Point Rule')
    plt.plot(mid_errors,label='Error in Mid-Point Rule')
    plt.plot(right_errors,label='Error in Right-Point Rule')
    plt.plot(trap_errors,label='Error in Trapezoidal Rule')
    plt.plot(simp_errors,label='Error in Simpson\'s Rule')
    plt.legend(loc='upper right')
    plt.xlabel('-- $i$ -->',fontsize=18)
    plt.ylabel('-- $I_i-I_{i-1}$ -->',fontsize=18)
    plt.title('Errors in Various Integration Algorithms',fontsize=20)
    plt.grid()
    plt.show()

if __name__=="__main__" :
    main()
