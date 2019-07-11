# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 10:13:46 2019

@author: Lisha Dsouza
"""

import numpy as np
import matplotlib.pyplot as plt
"""square of numbers"""
x=np.arange(1,11)
y=x**2
z=x**3

plt.subplot(121)
plt.plot(x,y,'r-o',label="first")
plt.subplot(122)
plt.plot(x,z,'b-o',label="second")
plt.legend()
plt.title("asdfadsF")
plt.xlabel("asdfasdF")
#%matplotlib auto
plt.show()