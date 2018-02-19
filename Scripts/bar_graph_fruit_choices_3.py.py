import matplotlib.pyplot as plt
import numpy as np

y = [9, 4, 1, 4, 15, 3]
x = [2, 4, 6, 8, 10, 12]
y2 = [3, 4, 1, 2, 4, 2]
x2 = [1.5, 3.5, 5.5, 7.5, 9.5, 11.5]
y3 = [ 6, 0, 0, 2, 11, 1]
x3 = [2.5, 4.5, 6.5, 8.5, 10.5, 12.5 ]
width = 1/1.5
fig = plt.figure()
ax = fig.add_subplot(111)
rext1 = ax.bar(x, y, width-1, color="blue", label = 'All people')
rect2 = ax.bar(x2, y2, width-1, color="red", label = 'Women')
rect3 = ax.bar(x3, y3, width-1, color="green", label = 'Males')
plt.title( 'Bar Graph for fruit choices', color = 'blue', fontsize = 14)
plt.grid(color= "green", linewidth= 0.15)
plt.legend(loc ="upper left", frameon= True )



ax.set_ylabel('Number of fruits', color = 'blue', fontsize = 12)
ax.set_xlabel('Fruit types',color = 'blue', fontsize = 12)
ax.set_xticks(x)
ax.set_xticklabels( ('Apple', 'Banana', 'Paw-paw', 'Grape','Pear', 'Guava' ), color = 'green' )

plt.show()

