# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 19:16:22 2016

@author: A30123
"""
import re

def yes_recipe(filename,string):
#    import re
    extract_regular_expression=re.search(string,filename)
    if extract_regular_expression is None:
        return 0
    else:
        return 1
        
AA = pd.read_csv("C://Users//A30123.ITRI//Documents//Python Scripts//A plus code//Try_20160112_check_Kaze_TS2_runs//TS2_event_list_PY.csv")
single_column =list(np.asarray(AA[:]['Current_list']))

recipe_yes_no_list = [yes_recipe(i,'DL_') for i in single_column]