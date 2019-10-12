from sklearn import datasets
import  numpy as np
"""
 Features : sepal length,sepal width, petal length, petal width
 Class labels : setosa ,versicolor , virginica
 [0,1,2]
"""

"""
Load dataset
"""
iris=datasets.load_iris()
#print(iris)

X=iris.data[:,[2,3]] # Select all rows but 2 columns of matrix
#print(x)
Y=iris.target;
print(np.unique(Y))

"""
Split dataset into train and test datasets

"""
from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)

#print(X_train)
# print(Y_test)
# print(Y_train)

"""
Feature scaling or standardizing using standardScale funtion of
 preprocessing module
"""

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
sc.fit(X_train)

X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)
#print(X_test_std)

from sklearn.linear_model import Perceptron
ptn=Perceptron(n_iter_no_change=40,eta0=0.1,random_state=0)
ptn.fit(X_train_std,Y_train)

pridiction=ptn.predict(X_test_std)

from sklearn.metrics import accuracy_score
print('Accuracy : %.2f' %accuracy_score(Y_test,pridiction))

#
# print(ptn)
#
# from sklearn.metrics import accuracy_score
#
# print(accuracy_score())
#
# from matplotlib import pyplot as plt

