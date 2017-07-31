import matplotlib.pyplot as plt
import numpy as np


def A7(title):
	y = [0, 85, 70, 60, 160, 160, 110, 60, 0 ]
	x = [x for x in range(len(y)) ]
	y_ticks = list(range(max(y)+2))

	# Format y_ticks
	def format_y_ticks():
		if max(y) < 30:	
			y_even = []
			for val in y_ticks:
				if val % 2 == 0:
					y_even.append(val)
		else:
			y_even = list(y_ticks[0:-1:20])
		return(y_even)

	y_vals = format_y_ticks()	
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(x, y, color="#FF00FF", ls='-', label='All people')

	#plot dots 
	start = 0
	for num in y:
		ax.scatter([x[start]], [y[start]], 10, color='lime')
		start += 1

	plt.title(title, color='blue', fontsize=14)
	plt.minorticks_on()
	plt.grid(color="blue", which='minor', linewidth=0.25, ls='--')
	plt.grid(color="blue", which='major', linewidth=0.25, ls='--')


	#plt.legend(loc="upper left", frameon=True )
	ax.set_ylabel('Distance \n (km)', color='blue', fontsize=12)
	ax.set_xlabel('Time (hrs)', color='blue', fontsize=12)
	ax.set_xticks(x)
	ax.set_yticks(y_vals)
	#ax.set_xticklabels(('Monday', 'Tuesday', 'Wed', 'Thursday', 'Friday',
	#'Saturday', 'Sunday'), color='green')

	plt.show()

A7('Nomvelo\'s drive in the countryside')