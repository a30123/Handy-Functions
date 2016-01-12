# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 16:29:41 2016

@author: A30123
"""
import csv
import numpy as np


def fetch_data_and_header2(file_path_name):
    with open(file_path_name,'rU') as csvfile:
        contents = csv.reader(csvfile)
        header_list = np.asarray(next(contents))
    
    number_of_sensors = len(header_list)   
    these_columns = range(1,number_of_sensors)
    table_values = np.loadtxt(file_path_name, delimiter=",",usecols = these_columns, skiprows=1)

    return table_values, header_list[1:]  
    
sensor_values, sensor_header = fetch_data_and_header2('E://MovedFromD//CSV//TS1//MFC_2492runs//current//run0880_450LED.450 LED 018_450LED.450 LED 018_897-current.csv')
sensor = "TMAl_1.source"
sensor_column = np.where(sensor_header==sensor)[0][0]
TMAl_1_source_data = sensor_values[:,sensor_column]
