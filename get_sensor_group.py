# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 17:20:43 2015

@author: A30123
"""
import re


def get_sensor_group(sensor_variable):
    group_string=re.search('^\w+.',sensor_variable)
    that_group=group_string.group(0)
    that_group=that_group.replace(".","")
    return that_group
    
#####example    
get_sensor_group('TMAl_1.source')
