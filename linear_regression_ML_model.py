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

#Any results you write to the current directory are saved as output.

#Example dataset, I don't have any actually data to work with 
#To import dataset file = directory to file where dataset located. Ex. = '\Downloads\tester' 
#Save locally or on server? 
data = pd.DataFrame({

    'Putrecine_Levels':[1.2,2.4,3.2,4.1,8.1],
    'pH_Levels':[1,2,3,4,8], 
    'Predicted_BV_Score':[1,2,3,4,10] #has to be predicated values/levels, pre-determined scale (Ex. 1 - 10) 

    }) 

#df = pd.read_cvs(data) 

#log transform putrescine 

#view the dimensions of the dataset, for when there's an atual dataset, and not just example data 
#df.shape 

#preview the dataset 
#df.head() 


#start graphing data 
#input 
X = data[[ 'pH_Levels', 'Putrecine_Levels']] 
#output 
Y = data['Predicted_BV_Score'] 

#model = LogisticRegression() 
model = LinearRegression() 
model.fit (X,Y) 

#Outputted Weights: 

weights = model.coef_  

#y - intercept 
intercept = model.intercept_ 

#ŷ 

BV_Rounded_Score = math.ceil(intercept)  
print("(For Debugging purposes), y - intercept (Unrounded):", intercept)
print("y-intercept (Around):", BV_Rounded_Score) 

# = β₀ = the log-odds when the X variable is 0, the baseline value for the log-odds of the event occurring, aka the y-intercept 
#log-odds = "A log odds in statistics is the logarithm of the odds ratio. Odds are likelihood ratios, and tell us how likely it is that something particular will happen." 

print("Weight for pH Levels:", weights[0]) 

print("Weight for Putrecine Levels:", weights[1]) 

plt.plot(X, Y) 
plt.show() 

#Linear regression equation = 'ŷ = b₀ + b₁x' 