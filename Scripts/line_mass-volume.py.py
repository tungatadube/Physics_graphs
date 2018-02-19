import matplotlib.pyplot as plt
import numpy as np


def A7(title):
    y = list(range(0, 111))
    x = y
    y_ticks = list(range(max(y)+2))
    x_ticks = list(range(max(x)+2))
    
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
            if max(x) < 30:	
                x_even = []
                for val in x_ticks:
                    if val % 2 == 0:
                        x_even.append(val)
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
    for num in y[0:-1:20]:
        ax.scatter([x[start]], [y[start]], 20, color='#000000')
        start += 20

    plt.title(title, color='blue', fontsize=14)
    plt.minorticks_on()
    plt.grid(color="#000000", which='minor', linewidth=0.4, ls='-')
    plt.grid(color="#000000", which='major', linewidth=0.7, ls='-')


    # plt.legend(lo
    # c="upper left", frameon=True )
    ax.set_ylabel(r'$\rm{Mass}$' '\n' r'$\rm{(g)}$', color='blue', fontsize=12)
    ax.set_xlabel(r'$\rm{Volume (cm^3)}$', color='blue', fontsize=12)
    ax.set_xticks(x_vals)
    ax.set_yticks(y_vals)
    #ax.set_xticklabels(('Monday', 'Tuesday', 'Wed', 'Thursday', 'Friday',
	#'Saturday', 'Sunday'), color='green')

    plt.show()

A7('Mass-Volume graph for water at room temperature')