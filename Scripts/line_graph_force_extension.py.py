import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mat


def spring_stiffness(title):
    '''
    The function plots an Extension to load graph for two springs that obey Ohm's law

    >>> E = F/K
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    '''

    # generate values of the forces

    F = np.arange(0.0, 250.0, 50.0)
    k = 10
    E = F/k



    plt.figure(figsize = (8,6), dpi= 100,)
    plt.plot(E, F, linewidth = 1.5, linestyle = '-', color = 'blue', label = 'Ductile material')
    t = 0
    plt.scatter([t,], [t/k,], 30, color = 'blue')
    plt.annotate(r'$O$', xy=(t, t/k), xycoords='data', xytext=(+20, +5), textcoords='offset points', fontsize=12, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

    F = np.arange(0.0, 500.0, 50.0)
    k = 50
    E = F/k
    plt.plot(E, F, linewidth = 1.5, linestyle = '-', color = 'green', label = "Stiff material")
    


    E = np.arange(20, 50.0, 0.05)
    k = 50
    F = 154*np.log10(E)
    plt.plot(E, F, linewidth = 1.5, linestyle = '-', color = 'blue',  )






    

    

    t = 20
    plt.scatter([t,], [154*np.log10(t),], 30, color = 'blue')
    plt.annotate(r'$ P $', xy=(t, 154*np.log10(t)), xycoords='data', xytext=(+10, +20), textcoords='offset points', fontsize=12, arrowprops=dict(arrowstyle= '->', connectionstyle='arc3, rad=.2'))
    t = 50
    plt.scatter([t,], [154*np.log10(t),], 30, color = 'red')
    plt.annotate(r'$B$', xy=(t, 154*np.log10(t)), xycoords='data', xytext=(+10, +20), textcoords='offset points', fontsize=12, arrowprops=dict(arrowstyle= '->', connectionstyle='arc3, rad=.2'))
   
    #plt.xticks(np.arange(10.0, 50.0, 5.0))
    #plt.yticks(np.arange(100, 500, 50))
    
    E = np.arange(1, 80.0, 0.5)
    k = 11
    F = 20*np.log(E)

  
    plt.plot(E, F, linewidth=1.5, linestyle='-', color='red', label="Plastic material")
    t = 50
    plt.scatter([t,], [154*np.log10(t),], 30, color = 'red')
 
    
    
    plt.grid(linewidth=0.2, color='green',)



    plt.title(title, color='blue')
    plt.ylabel('Force/N', color = 'green')
    plt.xlabel('Extension/mm', color = 'green')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.legend(loc= 'upper right', frameon= True, )


    plt.show()
    plt.close()
    plt.colormaps()

spring_stiffness('Fore Extension Graph for some materials')





