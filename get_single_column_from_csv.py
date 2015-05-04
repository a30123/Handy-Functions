# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:22:02 2015

@author: A30123
"""

def get_single_column_from_csv(csvpathfilename):
    import csv
    import numpy as np      
    
    thelist=[]
    
    with open(csvpathfilename,'rU') as csvfile:
        contents=csv.reader(csvfile)
        for row in contents:
            thelist.append(row[0])
        
    return np.array(thelist)    
    
##usage
uu=get_single_column_from_csv("C://Users//A30123.ITRI//Documents//Python Scripts//New_for_event_mining//Try_20150504_TMAl_source_setpoint_partition_rewritten//Output//CSV//1.csv")