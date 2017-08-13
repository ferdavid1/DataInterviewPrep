import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm
diabets = datasets.load_diabetes()
X_train, X_test, y_train, y_test = \
cross_validation.train_test_split(
diabets.data, diabets.target, test_size=0.2, random_state=0)
print (X_train.shape, y_train.shape) # test size 20%
print (X_test.shape, y_test.shape)
clf = svm.SVC(kernel='linear', C=1)
scores = cross_validation.cross_val_score(
clf, diabets.data, diabets.target, cv=4) # 4-folds
print (scores)
print("Accuracy: %0.2f (+/- %0.2f)" %(scores.mean(), scores.std()))
# wow, thats a a very shitty accuracy score