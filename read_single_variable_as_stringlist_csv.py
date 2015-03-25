# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 19:20:11 2015

@author: A30123
"""

######################################    
#alternative code for retrieving variable values
def read_single_variable_as_stringlist_csv(csvpathfilename, listofvariablename):
    import csv
    import numpy as np      
    
    notfirst=1
    thelist=[]
    
    with open(csvpathfilename,'rU') as csvfile:
        contents=csv.reader(csvfile)
        for row in contents:
            if notfirst==1:
               whichcolumn=row.index(listofvariablename)
               notfirst+=1
            else:
               thelist.append(row[(whichcolumn)])
        
    return np.array(thelist)    
######################################

########example##########################################################
StepLabelList=read_single_variable_as_stringlist_csv("E://TMAlgroup//setpoint//run1032_6 inch Si.SL.AlN_SLs Buffer_Si_017-4_6 inch Si.SL.AlN_SLs Buffer_Si_017-4_1046-setpoint.csv","StepLabel")

