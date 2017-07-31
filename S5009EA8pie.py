import matplotlib.pyplot as plt
from random import *


def pie_chart(title):
    ''' The function plots pie charts using the given data'''
    
    #Place your pie chart labels here
    labels = ['Oxygen', 'Silicon', 'Aluminium', 'Iron', 'Calcium', 
    'Sodium', 'Pottassium', 'Magnesium', 'Hydrogen', 'Titanium', 'Chlorine', 
    'Phosphorus', 'Strontium', 'Other'
    ]

    #Place your values here
    numbers = [49.2, 25.7, 7.5, 4.71, 3.39, 2.63, 2.40, 1.93, 0.87, 0.58, 0.19, 
    0.11, 0.09, 0.03]
    num = len(numbers)

    #A list of colors to chose from
    colors = ['#FF00FF', '#808080', '#000000', '#FF0000', '#800000', '#FFFF00',
    '#808000', '#00FF00', '#008000', '#800080', '#00FFFF', '#008080', '#0000FF',
     '#000080']

     # choose colors depending on the length of the given data
    #randomise the colors
    colorz = [x for x in sample(colors, num)]

    #This gets the sum of the values
    fracs = []
    total = float(0)
    for val in numbers:
        total += float(val)

    #And converts them to percentages if they are not. It stores the values in 
    # the variable fracs   
    for val in numbers:
        fracs.append((val/total)*100)   

    
    
    # have a ready explode iterable to recieve explode values in case you need
    # to explode a sector
    #Also keep the explode value with the same length as the original values
    explode = []
    for val in numbers:
        explode.append(0.00)

    # You can manipulate the wedge to explode here   
    explode[num-2] = 0.0


    pie, text =  plt.pie(fracs, shadow=True, explode=explode, colors=colorz)
    plt.title(title, color='blue', fontsize=14)
    #Make sure the piechart is a circle
    plt.axis('equal')
    #If more than one subplots, they must overlap
    plt.tight_layout()

    plt.legend(pie, labels, loc="best")
    
    
    plt.show()

pie_chart('Distribution of elements in the Earth\'s crust')