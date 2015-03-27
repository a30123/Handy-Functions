# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:38:28 2015

@author: A30123
"""
def extract_serial_number(filename):
    import re
    extract_regular_expression=re.search('(_\d+-setpoint)',filename)
    serial_number_string=extract_regular_expression.group(0)
    serial_number_string=serial_number_string.replace('-setpoint','')
    serial_number_string=serial_number_string.replace('_','') 
    value_of_number=int(serial_number_string)
    return value_of_number
    
    
##usage    

print('Reading CSV file:',extract_serial_number("run0001_CE_ON__1-setpoint"))