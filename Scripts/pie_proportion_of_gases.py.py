import matplotlib.pyplot as plt


def pie_chart(title):
    labels = ['Oxygen', 'Nitrogen', 'Other gases']

    numbers = [20, 79, 1]
    fracs = []
    total = float(0)
    for val in numbers:
        total += float(val)
      

    for val in numbers:
        fracs.append((val/total)*360)
       
    explode = [0, 0.0, 0.0]


    pie, text =  plt.pie(fracs, shadow=True, explode=explode)
    plt.title(title, color='blue', fontsize=14)
    plt.axis('equal')
    plt.tight_layout()
    plt.legend(pie, labels, loc="best")
    
    
    plt.show()

pie_chart('Proportion of gases in the atmosphere')