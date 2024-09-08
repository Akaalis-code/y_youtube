
import numpy 
import random
from y_plotting import *

var_axis_X = numpy.linspace(0, 100, num=100)
var_y = [random.randint(0,100) for _ in range(0,100) ]


sorting_y = var_y



for i in range(0,100) :
    for j in range(0,(len(var_y)-1)) :
        if sorting_y[j]>sorting_y[j+1] :
            temp = sorting_y[j]
            sorting_y[j] = sorting_y[j+1]
            sorting_y[j+1] = temp
        mth_plot(var_axis_X , sorting_y)
        pplt.pause(.000001)



pplt.show()

