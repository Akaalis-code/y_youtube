var_plot_file = 10

import matplotlib.pyplot as pplt

pplt.style.use('fivethirtyeight')

var_fig = pplt.figure()
var_figMgr = pplt.get_current_fig_manager()
var_figMgr.full_screen_toggle()

gs = var_fig.add_gridspec(1,1)
Axes1 = var_fig.add_subplot(gs[0, :])


def mth_plot(para_x , para_y):
    Axes1.cla()
    Axes1.bar(para_x, para_y, color='#6bbc6b')



#pplt.show()        Use this is calling file to start the plot viewing thread