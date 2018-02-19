import matplotlib.pyplot as plt
#% matplotlib inline


def pie_chart(title):
    labels = ['power stations and weapons testing', 'food', 'cosmic rays', 'medical', 'rocks', 'radon gas']

    numbers = [0.25, 0.4375, 0.4375, 0.4375, 0.4375, 4]
    fracs = []
    total = float(0)
    for val in numbers:
        total += float(val)
      

    for val in numbers:
        fracs.append((val/total)*360)
     
    explode = []
    for val in numbers: explode.append(0.00)


    pie, text =  plt.pie(fracs, shadow=True, explode=explode)
    plt.title(title, color='blue', fontsize=14)
    plt.axis('equal')
    plt.tight_layout()
    plt.legend(pie, labels, loc= 5)
    
    
    plt.show()

pie_chart('Sources of Background radiation')