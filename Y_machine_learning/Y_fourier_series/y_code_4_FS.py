import math
import numpy 
import scipy.integrate as integrate

var_axis_X = numpy.linspace(0, 6.28, num=10)
print(var_axis_X)
var_n = 10 # number of waves used for construction

var_a0 = 0 # a0 value
var_lst_an = ['NA'] # list of Cosine weightages
var_lst_bn = ['NA'] # list of Sine weightages


def mthd_get_coef(para_the_func , para_n ,para_an_or_bn):
    if para_n == 0 and para_an_or_bn == 'an':
        a0 = (0.3) * ((integrate.quad(lambda x:para_the_func(x) , -(math.pi) , (math.pi)))[0])
        return a0
    if para_n != 0 and para_an_or_bn == 'an':    
        an = (0.3) * ((integrate.quad((lambda x:para_the_func(x) * math.cos(para_n * x)) , -math.pi , math.pi))[0])
        return an
    if para_n != 0 and para_an_or_bn == 'bn':    
        bn = (0.3) * ((integrate.quad((lambda x:para_the_func(x) * math.sin(para_n * x)) , -math.pi , math.pi))[0])
        return bn
    return 'NA'

def mthd_output(para_n , para_a0 , para_lst_an , para_lst_bn , para_axis_X):
    f_of_x = (a0)*(1/2) 
    for cntr in range(1 , len(para_lst_an)+1) :
        f_of_x = f_of_x + para_lst_an[cntr] * (math.cos( (cntr) * (para_axis_X) ))

    for cntr in range(1 , len(para_lst_bn)+1) :
        f_of_x = f_of_x + para_lst_bn[cntr] * (math.sin( (cntr) * (para_axis_X) ))

var_the_func = math.sin
for i in range (0,var_n) :
    if i == 0 :
        var_a0 = mthd_get_coef(var_the_func , i , 'an')
    else :
        var_lst_an.append(mthd_get_coef(var_the_func , i , 'an'))
        var_lst_bn.append(mthd_get_coef(var_the_func , i , 'bn'))

print(var_a0 , var_lst_an , var_lst_bn)
