# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:44:01 2015

@author: A30123
"""
def get_varying_accuracy(max_flow,percentage_for_small_flow,percentage_for_large_flow,setpoint_values):
    yes_no=(setpoint_values<(0.25*max_flow))+0
    small_flow_part=yes_no*setpoint_values
    small_flow_accuracy=0.01*percentage_for_small_flow*small_flow_part
    
    no_yes=(setpoint_values>=(0.25*max_flow))+0
    large_flow_accuracy=(0.01*percentage_for_large_flow*max_flow)*no_yes
    
    varying_accuracy=large_flow_accuracy+small_flow_accuracy    
    
    return(varying_accuracy)
    
###### usage
    
get_varying_accuracy(500,0.25,1,setpoint_values):
   