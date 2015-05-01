# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:08:33 2015

@author: Mary
"""

def read_variables_as_stringlists_csv(csvpathfilename, variablenames):
    import csv
    import numpy as np      
    
    notfirst=1
    thelist=[]
    
    with open(csvpathfilename,'rU') as csvfile:
        contents=csv.reader(csvfile)
        for row in contents:
            if notfirst==1:
               print(row)
               whichcolumn=[row.index(i) for i in variablenames]
               notfirst+=1
            else:
               thelist.append([row[j] for j in whichcolumn])
        
    return np.array(thelist)    
######################################

########example##########################################################
List=read_variables_as_stringlists_csv("C://Users//Mary//Music//Documents//Python Scripts//Try_20150501_read_variables_as_stringlists_csv//run0015_CE_ON__15-setpoint.csv",["NH3_1.source","TMAl_1.source"])
list1=List[:,0]
list2=List[:,1]
