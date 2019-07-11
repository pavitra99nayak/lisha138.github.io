# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 10:07:34 2019

@author: Lisha Dsouza
"""

import numpy as np
a=np.random.randint(0,11,(4,4))
b=a.reshape((2,8))
c=a.reshape((a.shape[0]*a.shape[1],1))
print(a)
print(b)
print(c)