# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:09:25 2015

@author: Mary
"""

def get_positions(list_name,value_in_list):
#    import numpy as np    
    increments=np.array(range(len(list_name)))
    yes_equals_value=(list_name==value_in_list)
    return_this=increments[yes_equals_value]
    
    return return_this
    
cc=get_positions(np.array([0,2,3,3]),3)