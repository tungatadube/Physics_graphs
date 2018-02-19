import matplotlib.pyplot as plt
import numpy as np

def A7(title, blue, green, brown, other):

    y = [blue, green, brown, other]
    x = [2, 4, 6, 8]
    y_ticks = list(range(max(y)+2))

    

    # Format y_ticks
    def format_y_ticks():
        if max(y) < 30:	
            y_even = []
            for val in y_ticks:
                if val % 2 == 0:
                    y_even.append(val)
        else:		
            y_even = list(y_ticks[0:-1:5])
			
        return(y_even)

    y_vals = format_y_ticks()
    
    width = 1/1.5
    fig = plt.figure()
    ax = fig.add_subplot(111)
    rext1 = ax.bar(x, y, width-1, color="#FF00FF", label='All people')
    plt.title(title, color='blue', fontsize=14)
    plt.minorticks_on()
    plt.grid(color="#800080", which='major',linewidth=0.7, ls='-')
    #plt.grid(color='#800080', which='minor', lw=1.0, ls='-')
    #plt.legend(loc="upper left", frameon=True )
    ax.set_ylabel('Number of passengers', color='blue', fontsize=12)
    ax.set_xlabel('Destination',color='blue', fontsize=12)
    ax.set_xticks(x)
    ax.set_yticks(y_vals)
    ax.set_xticklabels(('USA', 'UK', 'SOUTH AFRICA', 'SPAIN', ), color='green')



    plt.show()

A7('Passenger-Destination Chart', 14, 10, 11, 5)