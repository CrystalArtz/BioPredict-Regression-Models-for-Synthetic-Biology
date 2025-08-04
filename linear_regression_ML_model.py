#A linear regression model example for use if needed, instead of a logistic regression model 

#Linear regression equation = 'ŷ = b₀ + b₁x₁ + b₂x₂' 
import numpy as np #linear algebra 
import pandas as pd #data processing 
import matplotlib.pyplot as plt #graphing 
import os #interact with operating system 
#import warnings #just incase 
from sklearn.linear_model import LinearRegression #import a Linear Regression ML model 

#Any results you write to the current directory are saved as output.


#Input data files that you want to test for score: 
#To import dataset file = directory to file where dataset located. Ex. = '\Downloads\tester' 
#Save locally or on server 
#Example data is shown 
#Some levels and factors must be known in order to first train the model 
data = pd.DataFrame({

    'Known_output_levels':[1.2,5.4,8.2,2.1,8.1],
    'Factor_1':[7,2,1,3,8], 
    'Factor_2':[0,1,0,1,1]

    }) 


#read the dataset 
df = pd.read_cvs(data) 

#Use to view the dimensions of the dataset 
df.shape 

#preview the dataset 
df.head() 


#start graphing data 
#input 
X = data[[ 'pH_Levels', 'Putrecine_Levels']] 
#output 
Y = data['BV_Levels'] 

model = LinearRegression() #defining that the type of model used is a Linear Regression type 
model.fit (X,Y) #fit the model to an x, y axis 

#Outputted Weights: 

weights = model.coef_ [0] 
intercept = model.intercept_[0]  

#b₀ 
print("b₀:", intercept) 

# = b₀ = the log-odds when the X variable is 0, the baseline value for the log-odds of the event occurring, aka the y-intercept 
#log-odds = "A log odds in statistics is the logarithm of the odds ratio. Odds are likelihood ratios, and tell us how likely it is that something particular will happen." 


#print the factors for the different weights 
#more or less weights can be added, depending on your needs 
print("Weight for factor 1 Levels:", weights[0]) #Print the weights of factor 1 

print("Weight for factor 2 Levels:", weights[1]) #Print the weights of factor 2 

#plot the data 
plt.plot(X, Y) 
plt.show() 
