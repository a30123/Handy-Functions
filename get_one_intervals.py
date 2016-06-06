# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 09:17:42 2016

@author: A30123
"""
import numpy as np

def consecutive(data, stepsize=1):
    return np.split(data, np.where(np.diff(data) != stepsize)[0]+1)
    
def extract_one_intervals(test_list):
    True_False_List = (np.asarray(test_list)==1)
    increment = np.array(range(len(test_list)))
    positions_of_ones = increment[True_False_List]
    group_of_consecutives = consecutive(positions_of_ones)
    list_of_intervals = [(min(i), (max(i)+1)) for i in group_of_consecutives]
    return(list_of_intervals)

def length_of_intervals(interval_as_tuple):
    return(interval_as_tuple[1]-interval_as_tuple[0])
    

if __name__ == '__main__':
    test_list = [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0] 
   
    one_intervals =  extract_one_intervals(test_list)
    print("one_intervals in occuring order: ", one_intervals)    
    
    one_intervals.sort(key=length_of_intervals)
    print("one_intervals in length sorted order:  ", one_intervals)
    
    top2 = one_intervals[-2:]
    print("top 2 longest one_interval:   ", top2)
    

    
    