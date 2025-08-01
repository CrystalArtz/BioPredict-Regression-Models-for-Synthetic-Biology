#Logistic regression equation = 'log(p / (1 - p)) = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ' 
import numpy as np #linear algebra 
import pandas as pd #data processing 
import matplotlib.pyplot as plt #graphing 
#import seaborn as sns # statistical data visualization 
import os #interact with operating system 
#import warnings #just incase lol 
from sklearn.linear_model import LogisticRegression 
#from sklearn.linear_model import LinearRegression 

#Input data files that you want to test for score (?): 

#for dirname, _, filenames in os.walk('/downloads/input'): #placeholder file directory 
    #for filename in filenames: 
        #print(os.path.join(dirname, filename)) 

#Any results you write to the current directory are saved as output.

#Example dataset, I don't have any actually data to work with 
#To import dataset file = directory to file where dataset located. Ex. = '\Downloads\tester' 
#Save locally or on server? 
data = pd.DataFrame({

    'Putrecine_Levels':[1.2,5.4,8.2,2.1,8.1],
    'pH_Levels':[7,2,1,3,8], 
    'BV_Levels':[0,1,0,1,1]

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
Y = data['BV_Levels'] 

model = LogisticRegression() 
#model = LinearRegression() 
model.fit (X,Y) 

#Outputted Weights: 

weights = model.coef_ [0] 
intercept = model.intercept_[0]  

#β₀ 
print("β₀:", intercept) 

# = β₀ = the log-odds when the X variable is 0, the baseline value for the log-odds of the event occurring, aka the y-intercept 
#log-odds = "A log odds in statistics is the logarithm of the odds ratio. Odds are likelihood ratios, and tell us how likely it is that something particular will happen." 

print("Weight for pH Levels:", weights[0]) 

print("Weight for Putrecine Levels:", weights[1]) 

#Logistic regression equation = 'log(p / (1 - p)) = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ' 

#plt.plot(X, Y) 
#plt.show() 
 
