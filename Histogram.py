# import matplotlib with the alias plt and numpy with the alias np
import numpy as np
import matplotlib.pyplot as plt

# reads data from our data file and stores it in the variable y
y = np.genfromtxt('data.txt', delimiter=',')


# the histogram of the data
n, bins, patches = plt.hist(y, 100, normed=1, facecolor='r', alpha=0.75)

# our labels and title
plt.xlabel('Amount of numbers')
plt.ylabel('Numbers Found')
plt.title('Histogram of data')

# show the grid
plt.grid(True)

# make the plot visible
plt.show()

