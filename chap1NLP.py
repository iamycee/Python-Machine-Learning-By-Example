from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

groups = fetch_20newsgroups()
#printing keys
groups.keys()    #you can do groups.key to print the values

#20 targets i.e. 20 newsgroups; data[n] will print the nth news post
groups.target_names[groups.target[0]]

#plotting for visualization

sns.distplot(groups.target)
plt.show()
#the distribution is fairly uniform

#for the unigram counts, we use the CountVectorizer class
cv = CountVectorizer(stop_words="english", max_features=500)    #see docs for details
#stop words are words like a, the, of, if

transformed = cv.fit_transform(groups.data)    #This is a list of 0s and 1s
print(cv.get_feature_names())


sns.distplot(np.log(transformed.toarray().sum(axis=0)))
plt.xlabel('Log Count')
plt.ylabel('Frequency')
plt.title('Distribution Plot of 500 word counts')

plt.show()
