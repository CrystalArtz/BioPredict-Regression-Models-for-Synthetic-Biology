#Linear regression equation = 'ŷ = b₀ + b₁x₁ + b₂x₂' 
import numpy as np #linear algebra 
import pandas as pd #data processing 
import matplotlib.pyplot as plt #graphing 
from sklearn.linear_model import LinearRegression #import and use a linear regression ML model 
import math #used for the linear regression model 
from logistic_regression_ML_model import intercept, weights #import the weights previously found using known data 


#Weights from Example_logistic_regression.py 
y_intercept = intercept  # intercept
factor_1_weight = weights[0]  # weight for factor 1 
factor_2_level = weights[1]  # weight for factor 2 

#Example values for an input 
test_factor_1_level = 3.0
test_factor_2_level = 5.5

#Calculating the Score based on previously found weights (example data is used) (Rounding up) 
full_score = y_intercept + factor_1_weight * test_factor_2_level + factor_2_level * test_factor_1_level 
rounded_score = math.ceil(full_score)

#printing the predicted score based on the found weights for the various factors based on known data 
print("Predicted disease 1 Score (Approximate):", full_score)
print("Predicted disease 1 Score (Rounded Up):", rounded_score) 
