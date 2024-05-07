import math
import numpy 
import scipy.integrate as integrate
from scipy import signal

import matplotlib.pyplot as pplt

var_axis_X = numpy.linspace(0, 6.28, num=50)
#var_axis_X = numpy.array(var_axis_X)
print('X axis list of values : ',var_axis_X)
var_n = 4 # number of waves used for construction

var_a0 = 0 # a0 value
var_lst_an = ['NA'] # list of Cosine weightages
var_lst_bn = ['NA'] # list of Sine weightages





def mthd_get_coef(para_the_func , para_n ,para_an_or_bn):
    # integrate.quad  is giving tuple as output , in which zero th index contains integration awnser
    if para_n == 0 and para_an_or_bn == 'an':
        a0 = (0.318) * ((integrate.quad(lambda x:para_the_func(x) , -(math.pi) , (math.pi)))[0])
        return a0
    if para_n != 0 and para_an_or_bn == 'an':    
        an = (0.318) * ((integrate.quad((lambda x:para_the_func(x) * math.cos(para_n * x)) , -math.pi , math.pi))[0])
        return an
    if para_n != 0 and para_an_or_bn == 'bn':    
        bn = (0.318) * ((integrate.quad((lambda x:para_the_func(x) * math.sin(para_n * x)) , -math.pi , math.pi))[0])
        return bn
    return 'NA'





def mthd_output(para_n , para_a0 , para_lst_an , para_lst_bn , para_axis_X):
    f_of_x = (para_a0)*(1/2) 
    for cntr in range(1 , len(para_lst_an)) :
        #print('f_of_x in an : ',f_of_x)
        f_of_x = f_of_x + para_lst_an[cntr] * (numpy.cos( (cntr) * (para_axis_X) ))

    for cntr in range(1 , len(para_lst_bn)) :
        #print('f_of_x in bn : ',f_of_x)
        f_of_x = f_of_x + para_lst_bn[cntr] * (numpy.sin( (cntr) * (para_axis_X) ))

    return f_of_x





def mth_plot_graph (para_axis_x , para_main_func , para_generated_func):
    pplt.plot(para_axis_x,para_main_func )
    pplt.plot(para_axis_x,para_generated_func )
    pplt.show()





var_the_func = signal.square
for i in range (0,var_n) :
    if i == 0 :
        var_a0 = mthd_get_coef(var_the_func , i , 'an')
    else :
        var_lst_an.append(mthd_get_coef(var_the_func , i , 'an'))
        var_lst_bn.append(mthd_get_coef(var_the_func , i , 'bn'))

print(' var_a0 : ',var_a0)
print(' var_lst_an : ',var_lst_an)
print(' var_lst_bn : ',var_lst_bn)





var_f_of_x = mthd_output(var_n , var_a0 , var_lst_an , var_lst_bn , var_axis_X)
print('var_f_of_x : ', var_f_of_x)





mth_plot_graph (var_axis_X , var_the_func(var_axis_X) , var_f_of_x)

