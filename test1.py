#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

xvalues = np.ogrid[17:27:0.1]
yvalues = np.ogrid[44:50:0.1]

Y=np.meshgrid(xvalues,yvalues)



print(Y[44,25])