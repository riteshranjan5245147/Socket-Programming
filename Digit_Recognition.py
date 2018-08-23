''' Digit Recognition Project '''

import matplotlib.pyplot as plt 

from sklearn import datasets
from sklearn import svm


digits = datasets.load_digits()

clf = svm.SVC(gamma=0.0001, C=100)

x,y = digits.data, digits.target

x_train = x[0:1700]
x_test = x[1700:]

y_train = y[0:1700]
y_test = y[1700:]

clf.fit(x_train, y_train)

pred = clf.predict(x_test)

c=0;

for i in range(0,len(y_test)):
    if pred[i]==y_test[i]:
        c=c+1


print 'accuracy is : ', (float(c)/len(y_test))*100
