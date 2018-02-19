import matplotlib.pyplot as plt
import numpy as np

y = [9, 4, 1, 4, 15, 3, 2]
x = [2, 4, 6, 8, 10, 12, 14]
y2 = [3, 4, 1, 2, 4, 2, 1]
x2 = [1.5, 3.5, 5.5, 7.5, 9.5, 11.5, 13.5]
y3 = [ 6, 0, 0, 2, 11, 1, 1]
x3 = [2.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5]
width = 1/1.5
fig = plt.figure()
ax = fig.add_subplot(111)
rext1 = ax.bar(x, y, width-1, color="blue",label= 'Women')
rect2 = ax.bar(x2, y2, width-1, color="red",label='Men')
rect3 = ax.bar(x3, y3, width-1, color="green",label='Children')
plt.title( 'Number of customers visiting a saloon', color = 'blue', fontsize = 14)
plt.grid(color= "green", linewidth= 0.15)
plt.legend(loc='upper left', frameon='True')


ax.set_ylabel('Number of People', color = 'blue', fontsize = 12)
ax.set_xlabel('Day of the week',color = 'blue', fontsize = 12)
ax.set_xticks(x)
ax.set_xticklabels( ('Sunday', 'Monday', 'Tuesday', 'Wed','Thursday', 'Friday', 'Saturday' ), color = 'green' )

plt.show()