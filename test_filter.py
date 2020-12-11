# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:17:15 2020

@author: clovi
"""
import clofredos_prj_inicio

if __name__ == "__main__":
    dataset = clofredos_prj_inicio.reading()
    filtered = clofredos_prj_inicio.score_done_filter(dataset,1000,True)
    
'''
filtro(dataset, score, done_status)
 
dataset: dataset in .csv format

score: the minimum score for the data to have and pass the filter

done_status: filters if the questions were solved or not.
"True" for solved and "False" for not solved
'''

