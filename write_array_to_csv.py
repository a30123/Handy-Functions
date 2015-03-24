# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:31:32 2015

@author: A30123
modified: Mar 24 2015
"""

##this function writes a list or an numpy array into (a) column(s) in csv
def write_array_to_csv(filename_path,listname):
    import csv
     
    runnumberfile=open(filename_path,'w',newline='')
    wr=csv.writer(runnumberfile,quoting=csv.QUOTE_ALL)
    if type(listname)==list:
        for item in listname:
            wr.writerow([item])
    elif type(listname)==np.ndarray:
        if len(listname.shape)==1:
            for item in listname:
                wr.writerow([item])
        else:
            for item in listname:
                wr.writerow(item)
    else:
        print("the structure you are writing is neither a list nor an np.ndarray")
		
    runnumberfile.close()
    
    
#################################################usage
import numpy as np    

write_array_to_csv("testwrite3.csv",np.array([[1,2,3],[3,4,5]]))

write_array_to_csv("testwrite4.csv",[1,2,3])

write_array_to_csv("testwrite5.csv",np.array([1,2,3]))

write_array_to_csv("testwrite6.csv","ko")