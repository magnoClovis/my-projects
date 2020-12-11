# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:21:17 2020

@author: clovi
"""

import clofredos_prj_inicio

if __name__ == "__main__":
    dataset = clofredos_prj_inicio.reading()
    max_score, max_score_index, max_value  = clofredos_prj_inicio.maximum(dataset)


