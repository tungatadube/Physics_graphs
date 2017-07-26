import matplotlib.pyplot as plt
import numpy as np

def A7(title, blue, green, brown, other):

	y = [blue, green, brown, other]
	x = [2, 4, 6, 8]
	y_ticks = list(range(max(y)))
	
	# Format y_ticks
	def format_y_ticks():
		if max(y) < 30:	
			y_even = []
			for val in y_ticks:
				if val % 2 == 0:
					y_even.append(val)
		else:		
			y_even = list(y_ticks[0:-1:5])
			
		return(y_even)
	
	y_vals = format_y_ticks()
		
	width = 1/1.5
	fig = plt.figure()
	ax = fig.add_subplot(111)
	rext1 = ax.bar(x, y, width-1, color="purple", label='All people')
	plt.title(title, color='blue', fontsize=14)
	plt.grid(color="blue", linewidth=0.25, ls='--')
	#plt.legend(loc="upper left", frameon=True )
	ax.set_ylabel('Number of pupils', color='blue', fontsize=12)
	ax.set_xlabel('Eye color',color='blue', fontsize=12)
	ax.set_xticks(x)
	ax.set_yticks(y_vals)
	ax.set_xticklabels(('Blue', 'Brown', 'Green', 'Hazel', ), color='green')

	plt.show()

A7('Mass of students in a class', 7, 3, 4, 19)