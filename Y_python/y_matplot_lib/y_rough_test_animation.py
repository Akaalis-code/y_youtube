from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation 

# initializing a figure in 
# which the graph will be plotted 
fig = plt.figure() 

gs = fig.add_gridspec(1,2)
Axes1 = fig.add_subplot(gs[0,0])
Axes2 = fig.add_subplot(gs[0,1])

# marking the x-Axes1 and y-Axes1 
#Axes1 = plt.axes(xlim =(0, 10), ylim =(-2, 2)) 
#Axes2 = plt.axes(xlim =(0, 4), ylim =(-2, 2)) 

# Setting the x and y limits for each subplot 
Axes1.set_xlim(0, 10)
Axes1.set_ylim(-2, 2)
Axes2.set_xlim(0, 4)
Axes2.set_ylim(0, 5)


# initializing a line variable 
line, = Axes1.plot([], [], lw = 3) 

# data which the line will 
# contain (x, y) 
def init(): 
	line.set_data([], []) 
	return line, 

def animate(i): 
	x = np.linspace(0, 4, 1000) 

	# plots a sine graph 
	y = np.sin(2 * np.pi * (x - 0.01 * i)) 
	line.set_data(x, y) 
	
	return line, 

anim = FuncAnimation(fig, animate, init_func = init, frames = 200, interval = 20, blit = True) 
import numpy
Axes2.plot([2,1,0,5,3,2])
#anim.save('continuousSineWave.mp4',writer = 'ffmpeg', fps = 30) 
plt.show()
