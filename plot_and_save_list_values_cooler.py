# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:16:15 2015

@author: A30123
"""
def ensure_dir(f):
    import os
    d=os.path.abspath(f)
    if not os.path.exists(d):
        os.makedirs(d)
  
def plot_and_save_list_values_cooler(valuelist,valuelist2,ll,rr,pathname,figure_filename):
    import matplotlib.pyplot as plt  #--------------------------------John Hunter's  2D plotting library
    from matplotlib import rc 
    import os
    import numpy as np
    
    rc('mathtext',default='regular')    
    
    ensure_dir(pathname)
    complete_path_to_save_figure=os.path.normpath(os.path.join(pathname,figure_filename))
    
    x_axis_range=np.arange(ll,rr)
    sub_valuelist=valuelist[ll:(rr)]
    sub_valuelist2=valuelist2[ll:(rr)]
    fig=plt.figure()
    ax=fig.add_subplot(111)
    
    lns1=ax.plot(x_axis_range,sub_valuelist,'-',label='left label ')
    
    ax2=ax.twinx()
    lns3=ax2.plot(x_axis_range,sub_valuelist2,'-r',label='right label')
    
    lns=lns1+lns3
    labs=[l.get_label() for l in lns]
    ax.legend(lns,labs,loc=0)
    
    ax.grid()
    ax.set_xlabel("time")
    ax.set_ylabel(r"vent.vac")
    ax2.set_ylabel(r"deviation")
    ax2.set_ylim(min(sub_valuelist2),max(sub_valuelist2))
    ax.set_ylim(min(sub_valuelist),max(sub_valuelist))    

    plt.show
    plt.savefig(complete_path_to_save_figure)
    plt.clf()
    
#usage
list1=np.arange(100)
list2=np.arange(100,0,-1)
left_end=45
right_end=75    
path_name="C://Users//A30123.ITRI//Documents//Python Scripts//New_for_event_mining//Try_20150430_plot_cooler_function_test"
file_name="coolplot.png"
plot_and_save_list_values_cooler(list1,list2,left_end,right_end,path_name,file_name)