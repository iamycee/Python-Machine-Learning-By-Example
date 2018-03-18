from sklearn.datasets import fetch_20newsgroups
from nltk.stem import WordNetLemmatizer
from nltk.corpus import names
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.svm import SVC
#MATPLOTLIB?
#import matplotlib.pyplot as plt
                                            #Add these for multiclass classification 
categories = ['comp.graphics', 'sci.space'] #, 'alt.atheism', 'talk.religion.misc', 'rec.sport.hockey']
data_train = fetch_20newsgroups(subset='train', categories=categories, random_state=42)
data_test = fetch_20newsgroups(subset='test', categories=categories, random_state=42)
#explicitly specifying the random state helps getting the same training and testing split

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
label_train = data_train.target
cleaned_test = cleanText(data_test.data)
label_test = data_test.target
print(len(cleaned_train))
print(len(label_train), len(label_test))

#It is good to see if classes are imbalanced, use counter for that
print(Counter(label_train))    #prints how many data points with 1 and how many with 0 label
print(Counter(label_test))

tfidf_vec = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english', max_features=8000)
term_docs_train = tfidf_vec.fit_transform(cleaned_train)    #term document matrix
term_docs_test = tfidf_vec.transform(cleaned_test)    #dont fit on the test set mate


svm = SVC(kernel='linear', C=1.0, random_state=42)    #linear kernel for our linearly separable data
svm.fit(term_docs_train, label_train)

accuracy = svm.score(term_docs_test, label_test)
print('The accuracy on testing set is: {0:.1f}%'.format(accuracy*100))

prediction = svm.predict(term_docs_test)
report = classification_report(label_test, prediction)
print(report)
























