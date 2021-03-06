import numpy as np
import matplotlib.pyplot as plt

def radioactive_decay(title):
    x = list(range(0,6))
    y = [4800*np.exp(-1*val)for val in x]
    plt.plot(x,y, 'ro-',  label = 'decay curve', markevery=1)
    plt.title(title, color='blue', fontsize=14)
    plt.minorticks_on()
    plt.grid(color="blue", which='major', linewidth=0.25, ls='-')
    plt.grid(color="grey", which='minor', linewidth=0.25, ls='--')
    plt.legend(loc="upper right", frameon=True )
    plt.ylabel('counts/hr')
    plt.xlabel('Time/hrs')
    plt.show()
    
radioactive_decay('Decay curve')