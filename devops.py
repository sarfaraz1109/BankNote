# -*- coding: utf-8 -*-
"""Devops.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Hv-7R_zitO2tuqPdYGchYTssIt7z4Mn
"""

# Commented out IPython magic to ensure Python compatibility.
#importing the required libraries 
import os
import numpy as np # importing for numeric operations
import pandas as pd # importing for data analysis


#importing libraries for visualization
import matplotlib.pyplot as plt # for data visualization & graphical plotting 
import seaborn as sns #for statistical graphics
# %matplotlib inline

from sklearn.model_selection import train_test_split #for splitting the data into train and test

## for standardize and Encoding the data
from sklearn.preprocessing import StandardScaler,OneHotEncoder

# for search the best parameter values from the given set of the grid of parameters
from sklearn.model_selection import GridSearchCV
import graphviz

from google.colab import drive
drive.mount('/content/drive')

import warnings
warnings.filterwarnings("ignore")

Bank_Data= pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Devops/BankNote_Authentication.csv')

Bank_Data.head()

Bank_Data.tail()

Bank_Data.describe()

Bank_Data.nunique()

X = Bank_Data.drop(["class"], axis =1)
y = Bank_Data["class"]

print(X.shape,y.shape)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=123,stratify=y)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

scaler = StandardScaler()

scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

Bank_Data.head()

"""# **LogisticRegression**"""

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score,classification_report

lr = LogisticRegression()
lr.fit(X_train,y_train)

train_pred=lr.predict(X_train)
test_pred=lr.predict(X_test)

def evaluate_model(act, pred):
    print("Confusion Matrix \n", confusion_matrix(act, pred))
    print("Accurcay : ", accuracy_score(act, pred))
    print("Recall   : ", recall_score(act, pred))
    print("Precision: ", precision_score(act, pred))

print("--Train--")
evaluate_model(y_train, train_pred)
print("--Test--")
evaluate_model(y_test, test_pred)

"""# **RandomForest**"""

from sklearn.ensemble import RandomForestClassifier

rm = RandomForestClassifier()
rm.fit(X_train,y_train)

train_pred=rm.predict(X_train)
test_pred=rm.predict(X_test)

def evaluate_model(act, pred):
    print("Confusion Matrix \n", confusion_matrix(act, pred))
    print("Accurcay : ", accuracy_score(act, pred))
    print("Recall   : ", recall_score(act, pred))
    print("Precision: ", precision_score(act, pred))

print("--Train--")
evaluate_model(y_train, train_pred)
print("--Test--")
evaluate_model(y_test, test_pred)

import pickle
pickle_out = open("lr.pkl","wb")
pickle.dump(lr,pickle_out)
pickle_out.close()

