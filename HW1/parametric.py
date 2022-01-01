# Program to plot several parametric curves together and use a legend to label them

import numpy as np
import matplotlib.pyplot as plt

def main() :
    # Defines necessary variables and plots the required parametric curves
    t=np.arange(0.0,2*np.pi,0.01)
    x1,y1=np.cos(t),np.sin(t)
    x2,y2=np.cos(3*t),np.sin(2*t)
    x3,y3=abs(np.cos(4*t))*np.cos(t),abs(np.cos(4*t))*np.sin(t)
    fig,ax=plt.subplots(1,1)

    ax.plot(x1,y1,label=r'$\mathbf{(a).}\:x=\cos t,\:y=\sin t$')
    ax.plot(x2,y2,label=r'$\mathbf{(b).}\:x=\cos 3t,\:y=\sin 3t$')
    ax.plot(x3,y3,label=r'$\mathbf{(c).}\:x=|\cos 4t|\:\cos t,\:y=|\cos 4t|\:\sin t$')
    ax.set_xlabel('-- x -->')
    ax.set_ylabel('-- y -->')
    ax.set_title('Parametric Plots using Matplotlib')
    ax.grid()
    ax.legend()
    plt.show()

if __name__=="__main__" :
    main()
