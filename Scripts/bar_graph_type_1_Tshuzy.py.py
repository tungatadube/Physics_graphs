import matplotlib.pyplot as plt
import numpy as np

def A7(title):
    y = [16, 10, 16, 15,20]
    x = [2, 4, 6, 8, 10]
    z = list(range(0,21))
    
    z2 = []
    for val in z:
        if val % 2 == 0:
            z2.append(val) 
   

    width = 1/1.5
    fig = plt.figure()
    ax = fig.add_subplot(111)
    rext1 = ax.bar(x, y, width-1, color="blue", label='All people')
    plt.title(title, color='blue', fontsize=14)
    plt.grid(color="green", linewidth=0.15)
    #plt.legend(loc="upper left", frameon=True )
    ax.set_ylabel('Sales', color='blue', fontsize=12)
    ax.set_xlabel('Day of the week',color='blue', fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(('Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday' ), color='green')
    ax.set_yticks(z2)

    plt.show()

A7('Weekday newspaper sales at Tshuzy Shopping center')

