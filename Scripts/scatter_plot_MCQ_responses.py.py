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
    F = [0, 1, 2, 3]
    L = [15.2, 16.2, 18.3, 18.6]
    E = [0.0, 1.0, 2.1, 3.4]
    plt.scatter(F, E, color = 'red')
    plt.grid(color='grey')
    plt.title(choices[3], color='blue')
    plt.ylabel('Extension/cm', color = 'blue')
    plt.xlabel('Force/N', color = 'blue')
    

    # Second response
    plt.subplot(2, 2, 2)
    F = [0, 1, 2, 3]
    L = [15.2, 16.9, 18.3, 18.6]
    E = [0.0, 1.0, 2.1, 3.4]

    plt.scatter(F, L, color = 'red')
    plt.grid(color='grey')
    plt.title(choices[1], color='blue')
    plt.ylabel('Extension/cm', color = 'blue')
    plt.xlabel('Force/N', color = 'blue')

    # Third response
    plt.subplot(2, 2, 3)
    F = [0, 1, 2, 3]
    L = [15.2, 16.2, 18.3, 18.6]
    E = [0.0, 1.5, 2.1, 3.4]
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