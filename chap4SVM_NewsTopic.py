from nltk.corpus import names
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV


categories = None
data_train = fetch_20newsgroups(subset='train', categories=categories, random_state=42)
data_test = fetch_20newsgroups(subset='test', categories=categories, random_state=42)

lemmatizer = WordNetLemmatizer()
all_names = set(names.words())
def letters_only(astr): 
    return astr.isalpha()

def cleanText(docs):
    cleaned_docs = []
    for doc in docs:
        cleaned_docs.append(' '.join(lemmatizer.lemmatize(word.lower()) for word in doc.split()
                             if letters_only(word) and word not in all_names))
        #lowercase everything, isalpha does number and punc. removal, not in all_names removes words
    return cleaned_docs

cleaned_train = cleanText(data_train.data)
cleaned_test = cleanText(data_test.data)
label_train = data_train.target
label_test = data_test.target

print(len(cleaned_train), len(label_train))
                             #scaling with log func., max document frequency  
tfidf_vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english', max_features=8000)

term_docs_train = tfidf_vectorizer.fit_transform(cleaned_train)
term_docs_test = tfidf_vectorizer.transform(cleaned_test)

svc_libsvm = SVC(kernel = 'linear')

parameters = {'C': (0.1, 1, 10, 100)}
grid_search = GridSearchCV(svc_libsvm, parameters, n_jobs=-1, cv=3)
#cv=3 means 3 fold cross validation, n_jobs=-1 means it runs parallelly on all available cores

import timeit
start_time = timeit.default_timer()
grid_search.fit(term_docs_train, label_train)

print("---%0.3f seconds---" %(timeit.default_timer - start_time))

#We can obtain the best parameter C by using
grid_search.best_params_

#We can obtain the best 30fold average performance under the optimal set of parameters:
grid_search.best_score_

#Retrieve the SVM model with the optimal parameter and apply it to the unknown testing set

svc_libsvm_best = grid_search.best_estimator_
accuracy = svc_libsvm_best.score(term_docs_test, label_test)

print("The accuracy on the testing set is : %.3f" %(accuracy*100))






















