import matplotlib.pyplot as plt


def pie_chart(title):
    labels = ['Rabbit', 'Monkey', 'Cat', 'Dog']

    numbers = [12, 6, 3, 3]
    fracs = []
    total = float(0)
    for val in numbers:
        total += float(val)
      

    for val in numbers:
        fracs.append((val/total)*360)
       
    explode = [0.0, 0.0, 0.0, 0.0] 


    plt.pie(fracs, shadow=True, explode=explode, labels=labels, autopct='% 1.0f%%',labeldistance=1.06, textprops=dict(color='navy', fontsize = 12))
    plt.title(title, color='blue', fontsize=14)
    plt.axis('equal')
    plt.tight_layout()
    #plt.legend(pie, labels, loc="best")
    
    
    plt.show()

pie_chart('Distribution of pupils by subject')