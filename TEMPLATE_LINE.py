
import matplotlib.pyplot as plt
import numpy as np


def A7(title):
    y = list(range(1,9))
    x = [0.40, 0.80, 1.20, 1.60, 2.00, 2.40, 2.80, 3.20]
    y_ticks = list(range(int(max(y)+2)))
    x_ticks = list(range(int(max(x)+2)))
    
    # Format y_ticks
    def format_y_ticks():
        if max(y) < 30:	
            y_even = []
            for val in y_ticks:
                if val % 2 == 0:
                    y_even.append(val)
        else:
            y_even = list(y_ticks[0:-1:20])
        return(y_even)

    def format_x_ticks():
            if max(x) < 5:	
                x_even = []
                for val in x_ticks:
                    x_even.append(int(val))
            else:
                x_even = list(x_ticks[0:-1:20])
            return(x_even)
        

    y_vals = format_y_ticks()
    x_vals = format_x_ticks()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, color="#FF00FF", ls='-', label='All people')

    #plot dots 
    start = 0
    for num in y:
        ax.scatter([x[start]], [y[start]], 20, color='#000000')
        start += 1

    plt.title(title, color='blue', fontsize=14)
    plt.minorticks_on()
    plt.grid(color="#000000", which='minor', linewidth=0.4, ls='-')
    plt.grid(color="#000000", which='major', linewidth=0.7, ls='-')


    # plt.legend(lo
    # c="upper left", frameon=True )
    ax.set_ylabel(r'$\rm{Force}$' '\n' r'$\rm{(N)}$', color='blue', fontsize=12)
    ax.set_xlabel(r'$\rm{Extension (mm)}$', color='blue', fontsize=12)
    ax.set_xticks(x_vals)
    ax.set_yticks(y_vals)
    #ax.set_xticklabels(('Monday', 'Tuesday', 'Wed', 'Thursday', 'Friday',
	#'Saturday', 'Sunday'), color='green')

    plt.show()

A7('Force-Extension graph')