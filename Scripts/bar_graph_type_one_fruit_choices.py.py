import matplotlib.pyplot as plt
import numpy as np

y = [9, 4, 1, 4, 15, 3]
x = [2, 4, 6, 8, 10, 12]

width = 1/1.5
fig = plt.figure()
ax = fig.add_subplot(111)
rext1 = ax.bar(x, y, width-1, color="blue", label='All people')
plt.title('Bar Graph for fruit choices', color='blue', fontsize=14)
plt.grid(color="green", linewidth=0.15)
plt.legend(loc="upper left", frameon=True )



ax.set_ylabel('Number of fruits', color='blue', fontsize=12)
ax.set_xlabel('Fruit types',color='blue', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels( ('Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday' ), color = 'green')

plt.show()

