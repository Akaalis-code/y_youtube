import math
import numpy 
import scipy.integrate as integrate
from scipy import signal

import matplotlib.pyplot as pplt

#print(pplt.style.available)
#pplt.style.use('dark_background')
pplt.style.use('fivethirtyeight')

var_fig = pplt.figure()
var_figMgr = pplt.get_current_fig_manager()
var_figMgr.full_screen_toggle()

gs = var_fig.add_gridspec(2,2)
Axes1 = var_fig.add_subplot(gs[0, :])
Axes2 = var_fig.add_subplot(gs[1, 0])
Axes3 = var_fig.add_subplot(gs[1, 1])


var_axis_X = numpy.linspace(0, 6.28, num=200)
var_n = 100 # number of waves used for construction

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




var_lst_f_of_X = []
def mthd_output(para_n , para_a0 , para_lst_an , para_lst_bn , para_axis_X):

    for cntr in range(0 , len(para_lst_an)) :
        if cntr == 0 :
            f_of_x = (para_a0)*(1/2) 
        else :
            #print('f_of_x in an : ',f_of_x)
            f_of_x = f_of_x + para_lst_an[cntr] * (numpy.cos( (cntr) * (para_axis_X) ))
            f_of_x = f_of_x + para_lst_bn[cntr] * (numpy.sin( (cntr) * (para_axis_X) ))
        var_lst_f_of_X.append(f_of_x)
    return f_of_x






def mth_plot_graph (para_axis_x , para_main_func , para_generated_func , para_cntr):
    Axes1.plot(para_axis_x,para_main_func )
    Axes1.plot(para_axis_x,para_generated_func)
    Axes1.text(0.5,-0.5,'Fourier series output')
    Axes1.text(0,-0.75,' a0 + sigma({an * COS(n*x)+bn * SIN(n*x)} , range-> 1 , Infinity)' , fontsize =  'small')
    #mth_sin_and_cosine_plot(var_a0 , var_lst_an , var_lst_bn , para_cntr)
    if para_cntr == 0 :
        Axes2.plot(para_axis_x , var_a0)
    else :
        Axes2.plot(para_axis_x , var_lst_an[para_cntr] * numpy.cos( para_cntr * para_axis_x))
        Axes3.plot(para_axis_x , var_lst_bn[para_cntr] * numpy.sin( para_cntr * para_axis_x))
        Axes2.text(0.5,-0.02,'an * COS(n*x)')
        Axes3.text(0.5,-0.75,'bn * SIN(n*x)')





var_the_func = signal.square
for i in range (0,var_n) :
    if i == 0 :
        var_a0 = mthd_get_coef(var_the_func , i , 'an')
    else :
        var_lst_an.append(mthd_get_coef(var_the_func , i , 'an'))
        var_lst_bn.append(mthd_get_coef(var_the_func , i , 'bn'))

for i in range (0,var_n):
    if i == 0 :
        if var_a0 < 0.05 :
            var_a0 = 0
    else :
        if var_lst_an[i] < 0.001:
            var_lst_an[i] = 0
        if var_lst_bn[i] < 0.001:
            var_lst_bn[i] = 0


var_f_of_x = mthd_output(var_n , var_a0 , var_lst_an , var_lst_bn , var_axis_X)




array=numpy.array
for i in range(1,len(var_lst_f_of_X)) :
    Axes1.cla()
    mth_plot_graph (var_axis_X , var_the_func(var_axis_X) , var_lst_f_of_X[i] , i)
    pplt.pause(.01)

pplt.show()