# Program to plot histograms with randomly generated data

import numpy as np
import matplotlib.pyplot as plt

def main() :
    # Defines necessary variables and plots the required histograms
    uniform=np.random.rand(1000)
    normal=np.random.normal(0.0,1.0,1000)

    fig,ax=plt.subplots(1,2)

    ax[0].hist(uniform,rwidth=0.95,color='cornflowerblue')
    ax[0].grid()
    ax[0].set_xlabel('-- x -->')
    ax[0].set_xticks(np.arange(0.0,1.1,0.1))
    ax[0].set_ylabel('-- Frequency of x -->')
    ax[0].set_title('Distribution of 1000 samples from a Uniform Distribution over [0,1)')

    ax[1].hist(normal,rwidth=0.95,color='forestgreen')
    ax[1].grid()
    ax[1].set_xlabel('-- x -->')
    ax[1].set_xlim([-2.0,2.0])
    ax[1].set_ylabel('-- Frequency of x -->')
    ax[1].set_title('Distribution of 1000 samples from a Normal Distribution with 0 mean and unit standard deviation')

    plt.show()

if __name__=="__main__" :
    main()
