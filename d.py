import matplotlib.pyplot as plt
import numpy as np


choices = [1, 2, 3, 4]
def plotter(** choices):
    '''The function plots responses for pupils in an MCQ question'''

    # First response

    plt.figure(1)
    plt.title('Choose the correct graph', color='blue', fontsize=14,)
    plt.subplot(2, 2, 4)
    choices = [1, 2, 3, 4]
    F = [0, 10, 20, 30]
    L = [50.0, 52.1, 54.1, 56.3]
    E = [0.0, 2.1, 4.0, 6.3]
    plt.scatter(F, E, color = 'red')
    plt.grid(color='grey')
    plt.title(choices[3], color='blue')
    plt.ylabel('Extension/cm', color = 'blue')
    plt.xlabel('Force/N', color = 'blue')
    

    # Second response
    plt.subplot(2, 2, 2)
    F = [0, 10, 20, 30]
    L = [50.0, 53.1, 54.1, 56.3]
    E = [0.0, 2.1, 4.0, 6.3]

    plt.scatter(F, L, color = 'red')
    plt.grid(color='grey')
    plt.title(choices[1], color='blue')
    plt.ylabel('Extension/cm', color = 'blue')
    plt.xlabel('Force/N', color = 'blue')

    # Third response
    plt.subplot(2, 2, 3)
    F = [0, 10, 20, 30]
    L = [50.0, 52.1, 54.1, 56.3]
    E = [0.0, 2.5, 4.0, 6.3]
    plt.scatter(F, E, color = 'red')
    plt.grid(color='grey')
    plt.title(choices[2], color='blue')
    plt.ylabel('Extension/cm', color = 'blue')
    plt.xlabel('Force/N', color = 'blue')

    # Fourth response
    plt.subplot(2, 2, 1)

    plt.scatter([F,], [L,], 30, color = 'red')
    plt.grid(color='grey')
    plt.title(choices[0], color='blue')
    plt.ylabel('Extension/cm', color = 'blue')
    plt.xlabel('Force/N', color = 'blue')

    plt.tight_layout(pad = 1.08)
    plt.show()

plotter()