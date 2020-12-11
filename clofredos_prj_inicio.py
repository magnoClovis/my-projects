# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 08:55:33 2020

@author: clovi
"""

import pandas as pd
import numpy as np
import csv 
from tqdm import tqdm

''''
All three functions here will be runned by other programs for testing and analyzing the obtained results


The "reading" function  is responsible for reading the dataset using pandas and return the dataset already
opened. 
'''
def reading():
    data = "full_dataset_v5_1.csv"
    dataset = pd.read_csv(data)
    return dataset
    

''' 
The "score_done_filter" function filters the dataset acording to the score that each question has in
the data and the "done" status, it is possible to set the minimum score and the status of the questions 
to look for and filter. The scores are integers, and the status booleans being possible to use one of both 
"True" or "False" values for filtering the data. The filtered data is stored in a numpy array and the function
returns that array as a result of the filter
'''
def score_done_filter(dataset, score, done_status):
    fill = dataset[:0] 
    for item in tqdm(range(len(dataset))):
        if dataset["score"][item] > score and dataset["done"][item] == done_status:
            fill = np.append(fill, dataset[item:item+1], axis = 0)
    return fill


'''
The "minimum" and "maximum" functions are quite similars. They, respectively, look for the lower and higher
scores in the dataset and return those scores, where it is located in the dataset and also returns the complete
data of the question with that specific score
'''
def minimum(dataset):
    min_score = dataset[:1]
    min_score_index = 0
    for item in tqdm(range(len(dataset))):
        if ((dataset["score"][item]) < (dataset["score"][min_score_index])):
            min_score = dataset[:0]
            min_score = np.append(min_score, dataset[item:item+1], axis=0)
            min_score_index = item
            min_value = dataset["score"][item]
        elif ((dataset['score'][item]) == (dataset["score"][min_score_index])):
            min_score = np.append(min_score, dataset[item:item+1], axis=0)
            min_value = dataset["score"][item]
    return min_score, min_score_index, min_value


def maximum(dataset):
    max_score = dataset[:1]
    max_score_index = 0
    for item in tqdm(range(len(dataset))):
        if ((dataset["score"][item]) > (dataset["score"][max_score_index])):
            max_score = dataset[:0]
            max_score = np.append(max_score, dataset[item:item+1], axis=0)
            max_score_index = item
            max_value = dataset["score"][item]
        elif ((dataset['score'][item]) == (dataset["score"][max_score_index])):
            max_score = np.append(max_score, dataset[item:item+1], axis=0)
            max_value = dataset["score"][item]
    
    return max_score, max_score_index, max_value
