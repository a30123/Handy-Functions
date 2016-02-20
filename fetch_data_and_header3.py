# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:40:52 2016

@author: Mary
"""

        
def fetch_data_and_header3(file_path_name, dtype=float):
    table_values = np.genfromtxt(file_path_name, dtype=dtype, delimiter=",", skiprows=1)
    with open(file_path_name,'rU') as csvfile:
        contents = csv.reader(csvfile)
        header_list = np.asarray(next(contents))
    
    return table_values, header_list    
    