# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:27:53 2016

@author: A30123
"""

def extract_serial_number_ultimate(filename,tail_string):
    extract_regular_expression=re.search('(_\d+)'+tail_string,filename)
    serial_number_string=extract_regular_expression.group(0)
    serial_number_string=serial_number_string.replace(tail_string,'')
    serial_number_string=serial_number_string.replace('_','') 
    value_of_number=int(serial_number_string)
    return value_of_number 
    
def extract_serial_number_ultimate(filename, tail_string="-current.csv"):
    extract_regular_expression = re.search('(_\d+'+tail_string+'$)',filename)
    serial_number_string = extract_regular_expression.group(0)
    serial_number_string = serial_number_string.replace(tail_string,'')
    serial_number_string = serial_number_string.replace('_','') 
    value_of_number = int(serial_number_string)
    return value_of_number 