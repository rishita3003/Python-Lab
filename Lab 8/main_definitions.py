# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:14:35 2024

@author: Rishita Agarwal
220150016
Graded Lab 8

"""

import arithmetic_op

def main(a,b):
    c=arithmetic_op.arithmetic_sum(a, b)
    d=arithmetic_op.arithmetic_mul(a, b)
    return c,d
    
if __name__ =='__main__':
    a=5
    b=3
    c,d= main(a,b)
    
