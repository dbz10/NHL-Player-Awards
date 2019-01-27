# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:58:21 2019

@author: celad
"""

import pandas as pd

hockey_path = 'C:\\Users\\celad\\Google Drive\\Documents\\Research\\stunning-parakeet'
data = pd.read_csv(hockey_path)
data.describe()