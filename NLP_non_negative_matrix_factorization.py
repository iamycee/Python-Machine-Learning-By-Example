from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import NMF
from nltk.corpus import names
from nltk.stem import WordNetLemmatizer
import numpy as np

def letters_only(astr):
    return astr.isalpha()

#Vectorizes to values where 0 if present and 1 if absent
cv = CountVectorizer(stop_words="english", max_features=500)
groups = fetch_20newsgroups()
cleaned = []
all_names = set(names.words())
lemmatizer = WordNetLemmatizer()

for post in groups.data:
    cleaned.append(' '.join([lemmatizer.lemmatize(word.lower()) for word in post.split()
                             if letters_only(word) and word not in all_names]))

#vector needed as ML algorithm does not know what text is, so converts into numerical vector
transformed = cv.fit_transform(cleaned)    #Vectorizes to values where 0 if present and 1 if absent
nmf = NMF(n_components=100, random_state=43).fit(transformed)    #non negative matrix factorization; V = WH;

for topic_idx, topic in enumerate(nmf.components_):
    label = '{}: '.format(topic_idx)
    print(label, " ".join([cv.get_feature_names()[i] for i in topic.argsort()[:-9:-1]]))


    
