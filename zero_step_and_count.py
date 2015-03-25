# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 2015

@author: A30330 HCKu
"""
def zero_step_and_count(steplabel_file_path):
    import numpy as np    
    xxx=get_variable_from_csv_alternative(steplabel_file_path, 'StepLabel')##needs another function!!
    mmm=np.zeros((np.shape(xxx)[0],1))
    mmmm=np.zeros((np.shape(xxx)[0],1))
        
    for i in range(len(mmm)):
        mmm[i]=xxx[i].split(".")[0]
        try:
            mmmm[i]=xxx[i].split(".")[1]
        except:
            mmmm[i]=0
        
    zero_step=0
    for i in range(len(mmm)-1):
        if mmm[i]>mmm[i+1]:
            zero_step=(i+1)
            break
        elif mmm[i]==mmm[i+1] and mmmm[i]>mmmm[i+1]:
            zero_step=(i+1)
            break
                
    return((len(xxx)-int(zero_step))), mmm
    
###### usage
zero_step,mmm=zero_step_and_count("E://MovedFromD//CSV//TS1//MO1group_line_run_2363runs//setpoint//run0776_Bake_Bake_792-setpoint.csv") 
  