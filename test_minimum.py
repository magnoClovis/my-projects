# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:24:31 2020

@author: clovi
"""

import clofredos_prj_inicio

if __name__ == "__main__":
    dataset = clofredos_prj_inicio.reading()
    min_score, min_score_index, min_value  = clofredos_prj_inicio.minimum(dataset)