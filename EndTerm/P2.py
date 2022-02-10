# Problem 2

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import interpolate

def y(x,r) :
    return ((r**2-x**2)**(1/2))

def main() :
    # part a. : finds area of a circle of radius 10
    area=2*integrate.romberg(y,-10,10,args=(10,),divmax=17) # multiplied by 2 as this is only the area of upper semi-circle
    print("\nArea of a circle of radius 10 is",area)

    # part b. : plots the area for different radii
    radii,areas=np.linspace(5,50,10),np.zeros(10)
    for i in range(10) :
        areas[i]=2*integrate.romberg(y,-radii[i],radii[i],args=(radii[i],),divmax=17)
    plt.plot(radii,areas)
    plt.xlabel('-- Radius r -->') 
    plt.ylabel('-- Area A -->')
    plt.title('Variation of Area of a Circle with it\'s Radius')
    plt.grid()
    plt.show()

    # part c. : interpolates the areas found in b. and finds the area of a circle of radius 13 using the interpolation
    interp=interpolate.CubicSpline(radii,areas)
    print('\nThe area of a circle of radius 13 found by interpolating the data is',interp(13))

if __name__=="__main__" :
    main()
