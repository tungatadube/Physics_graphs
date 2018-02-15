import numpy as np
import matplotlib.pyplot as plt

def radioactive_decay(title):
    x = [0, 30, 60, 90, 120, 150, 180]
    y = [100, 69, 47, 32, 22, 15, 10]
    plt.plot(x,y, 'ro-',  label = 'decay curve', markevery=1)
    plt.title(title, color='blue', fontsize=14)
    plt.minorticks_on()
    plt.grid(color="blue", which='major', linewidth=0.25, ls='-')
    plt.grid(color="grey", which='minor', linewidth=0.25, ls='--')
    plt.legend(loc="upper right", frameon=True )
    plt.ylabel('counts/min')
    plt.xlabel('Time/s')
    plt.show()
    
radioactive_decay('Decay curve')