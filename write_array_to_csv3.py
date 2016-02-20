# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 16:00:27 2016

@author: Mary
"""

def write_array_to_csv(filename_path, listname):
#    import csv 
#    import numpy as np
    with open(filename_path, 'w', newline='') as csvfile:
        wr = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
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
    