# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:15:55 2015

@author: Mary
"""

def get_matrix_from_csv(csvpathfilename):
#    import csv
#    import numpy as np      
    
    thelist=[]
    
    with open(csvpathfilename,'rU') as csvfile:
        contents=csv.reader(csvfile)
        for row in contents:
            thelist.append(row)
        
    return np.array(thelist)  