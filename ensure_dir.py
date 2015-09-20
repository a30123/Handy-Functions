# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:36:17 2015

@author: A30123
"""

def ensure_dir(f):
#    import os
    d=os.path.abspath(f)
    if not os.path.exists(d):
        os.makedirs(d)