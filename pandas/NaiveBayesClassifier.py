import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn import metrics

df = pd.read_csv('your_data_set.csv')

X = df.drop(['feature_1','feature_2','...'],axis=1)
y = df['target']

# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33)

#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(X_test)

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
