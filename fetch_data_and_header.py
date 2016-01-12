# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 16:31:54 2016

@author: A30123
"""

import csv
import numpy as np

def fetch_data_and_header(file_path_name):
    table_values = np.loadtxt(file_path_name, delimiter=",", skiprows=1)

    with open(file_path_name,'rU') as csvfile:
        contents = csv.reader(csvfile)
        header_list = np.asarray(next(contents))
    
    return table_values, header_list