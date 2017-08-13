from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np 

categories = ['alt.atheism']
newsgroups_train = fetch_20newsgroups(subset='train', categories= categories)
count_vect=CountVectorizer()
Train_counts = count_vect.fit_transform(newsgroups_train.data) # creating the sparse matrix
print(count_vect.vocabulary_.get(u'house')) # same output as next line
print(list(count_vect.get_feature_names()).index('house')) # same output as previous line