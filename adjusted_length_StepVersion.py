# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 09:43:54 2015

@author: A30330 HCKu
"""
def adjusted_length(step_file_path):
    import numpy as np
    
    mm=get_variables_from_csv(step_file_path, ['Step'])##needs another function!!
    
    nonzero_step=np.zeros((1,1))
    if min(mm)==0:
        zero_step=np.count_nonzero(mm==0)
        if zero_step==len(mm):
            zero_step=0
    else:
        nonzero_step=np.count_nonzero(mm==min(mm))
        for i in range(len(mm)):
            if mm[i]==min(mm):
                zero_step=(i+1)-nonzero_step
                
    return((len(mm)-int(zero_step)))
    
###### usage
modified_length=adjusted_length("E://MovedFromD//CSV//TS1//MO1group_line_run_2363runs//setpoint//run0776_Bake_Bake_792-setpoint.csv") 
shortened_data=original_data[-modified_length:]  