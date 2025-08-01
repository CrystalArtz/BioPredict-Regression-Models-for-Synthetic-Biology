#Linear regression equation = 'ŷ = b₀ + b₁x₁ + b₂x₂' 
import numpy as np #linear algebra 
import pandas as pd #data processing 
import matplotlib.pyplot as plt #graphing (Not needed, using sklearn lol)
#import seaborn as sns # statistical data visualization 
import os #interact with operating system 
#import warnings #just incase lol 
#from sklearn.linear_model import LogisticRegression 
from sklearn.linear_model import LinearRegression 
import math 
from Example_logistic_regression import intercept, weights 


#Weights from Example_logistic_regression.py 
y_intercept = intercept  # intercept
pH_weight = weights[0]  # weight for Putrescine_Levels
putrescine_level = weights[1]  # weight for pH_Levels

#Example values for an input 
test_putrescine_level = 3.0
test_pH_level = 5.5

#Calculating BV Score (Rounding up) 
full_score = y_intercept + pH_weight * test_putrescine_level + putrescine_level * test_pH_level 
rounded_score = math.ceil(full_score)

print("Predicted BV Score (Around):", full_score)
print("Predicted BV Score (Rounded Up):", rounded_score) 



