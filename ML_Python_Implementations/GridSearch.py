from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.grid_search import GridSearchCV
from sklearn import datasets
import numpy as np

# load toy dataset
boston = datasets.load_boston()

X, y = boston.data, boston.target
yint = y[:].astype(int)

# grid = 20 x 2 x 3
classifier = KNeighborsClassifier(n_neighbors=5, weights='uniform', metric='minkowski', p=2)

grid = {'n_neighbors': list(range(1,11)), 'weights': ['uniform', 'distance'], 'p': [1,2]}

print('baseline: {}'.format(np.mean(cross_val_score(classifier, X, yint, cv=10, scoring='accuracy', n_jobs=1)))) # 10 fold accuracy

search = GridSearchCV(estimator=classifier, param_grid=grid, scoring='accuracy', n_jobs=1, refit=True, cv=10)

search.fit(X, yint) # grid search across paramters for classifier

print("Best Parametes: {}".format(search.best_params_))
print("Accuracy: {}".format(search.best_score_))

'''
baseline: 0.1363100190200291
Best Parametes: {'n_neighbors': 10, 'p': 1, 'weights': 'distance'}
Accuracy: 0.15217391304347827
'''