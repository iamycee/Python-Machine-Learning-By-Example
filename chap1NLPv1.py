#IMPLEMENTING STEMMING I.E LEMMATIZATION
#KMeans clustering too

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import names
from nltk.stem import WordNetLemmatizer
from sklearn.cluster import KMeans

def letters_only(astr): 
    return astr.isalpha()

groups = fetch_20newsgroups()
#printing keys
#groups.keys()    #you can do groups.key to print the values

#20 targets i.e. 20 newsgroups; data[n] will print the nth news post
#groups.target_names[groups.target[0]]
cleaned = []
all_names = set(names.words())    #set will have only unique values
lemmatizer = WordNetLemmatizer()


for post in groups.data:
    cleaned.append(' '.join([lemmatizer.lemmatize(word.lower()) for word in post.split()
                             if letters_only(word) and word not in all_names]))
    
#plotting for visualization
 
##sns.distplot(groups.target)
##plt.show()
#the distribution is fairly uniform

#for the unigram counts, we use the CountVectorizer class
#CV class converts words into a learned vocabulary and  makes a
#numerical array to feed into the algorithm
cv = CountVectorizer(stop_words="english", max_features=500)    #see docs for details
#stop words are words like a, the, of, if

transformed = cv.fit_transform(cleaned)
plt.scatter(transformed)
#print(cv.get_feature_names())

km = KMeans(n_clusters=20)      #try different values
km.fit(transformed)
labels = groups.target
plt.scatter(labels, km.labels_)
plt.xlabel('Newsgroup')
plt.ylabel('Cluster')
plt.show()


##sns.distplot(np.log(transformed.toarray().sum(axis=0)))
##plt.xlabel('Log Count')
##plt.ylabel('Frequency')
##plt.title('Distribution Plot of 500 word counts')
##
##plt.show()
