import os
import glob
import numpy as np


emails, labels = [], []
#To load and label the spam email files to label '1'
spam_file_path = 'enron1/spam'
for filename in glob.glob(os.path.join(spam_file_path, '*.txt')):
    with open(filename, 'r',  encoding= 'ISO-8859-1') as infile:
        emails.append(infile.read())
        labels.append(1)

#To load and label the non spam email files to label '0'
ham_file_path = 'enron1/ham'
for filename in glob.glob(os.path.join(ham_file_path, '*txt')):
    with open(filename, 'r', encoding='ISO-8859-1') as infile:
        emails.append(infile.read())
        labels.append(0)

##Data preprocessing-
##1. Number and punctuation removal
##2. Human name removal
##3. Stop words removal
##4. Lemmatization
from nltk.corpus import names
from nltk.stem import WordNetLemmatizer

def letters_only(astr): 
    return astr.isalpha()
all_names = set(names.words())
lemmatizer = WordNetLemmatizer()

def cleanText(docs):
    cleaned_docs = []
    for doc in docs:
        cleaned_docs.append(' '.join(lemmatizer.lemmatize(word.lower()) for word in doc.split()
                             if letters_only(word) and word not in all_names))
        #lowercase everything, isalpha does number and punc. removal, not in all_names removes words
    return cleaned_docs



 
##print("\t\t---BEFORE CLEANING---\n\n\n")
##print(emails[0])
cleaned_emails = cleanText(emails)
#print("\n\n\n\n\t\t---AFTER CLEANING---\n\n")
#print(cleaned_emails[:3])    #print the first 3 cleaned emails

#to remove stop words use count vectorizer
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(stop_words="english", max_features=500)

#The vectorizer turns the document matrix into TERM DOCUMENT MATRIX where each row
#is a term frequency sparse vector for a document and an email
#The sparse vector is in the form of (row_index, feature/word_index) (word frequency)
    #term_docs = cv.fit_transform(cleaned_emails)
#print(term_docs[0])

#To see the correspoding terms are from the feature_index do:
#feature_names = cv.get_feature_names()
#print("Word at index 481 is: {}".format(feature_names[481]))   #put the index value as the argument    


#---WITH ALL THE PREPROCESSING DONE, we can now build our Naive Bayes model---

def get_label_index(labels):
    
    from collections import defaultdict
    label_index = defaultdict(list)    #label_index is a dictionary
    for index, label in enumerate(labels):
        label_index[label].append(index)        #appends the indices of the mails to 0 and 1 keys in the dict 
    return label_index

#label_index = get_label_index(labels)

def get_prior(label_index): 
    prior = {label:len(index) for label, index in label_index.items()}     #len index is just no. of emails under each 0, 1 category
    print(prior)
    total_count = sum(prior.values())
    for label in prior:
        #both labels are divided by the total
        prior[label] /= float(total_count)    #x= x/n ::= x /= n
    return prior    #dictionary with class label as key and corresponsiing prior as value


#prior = get_prior(label_index)
#print(prior)

def get_likelihood(term_document_matrix, label_index, smoothing=0):
    likelihood= {}    #empty dict; class : P(feature|class)
    for label, index in label_index.items():
        #calculate sum of 0 values and 1 values
        likelihood[label] = term_document_matrix[index, :].sum(axis=0) + smoothing    #smoothing used to adjust for 0 values
        likelihood[label] = np.asarray(likelihood[label])[0]
        total_count = likelihood[label].sum()
        likelihood[label] = likelihood[label] / float(total_count)    #term frequency / total frequency of all terms
        #likelihood[label] has #term frequency / total frequency or P(feature | class)  --- label [0] for ham, [1] for spam
    return likelihood    #dictionary with class label as key and corresponding conditional P(feature|class) as value

smoothing = 1
#likelihood = get_likelihood(term_docs, label_index, smoothing)
#print(likelihood[0][:5])

def get_posterior(term_document_matrix, prior, likelihood):
    num_docs = term_document_matrix.shape[0]
    posteriors = []
    for i in range(num_docs):
    #posterior is propostional to prior and likelihood
    #posterior = exp(log(prior * likelihood))       #for easy calculation, faster.
        posterior = {key: np.log(prior_label) for key, prior_label in prior.items()}
        for label, likelihood_label in  likelihood.items():
            term_document_vector = term_document_matrix.getrow(i)   #take single row 
            counts = term_document_vector.data
            indices = term_document_vector.indices
            for count, index in zip(counts, indices):
                posterior[label] += np.log(likelihood_label[index]) * count
        min_log_posterior = min(posterior.values())
        for label in posterior:
            try:
                posterior[label] = np.exp(posterior[label] - min_log_posterior)
            except:
                #if  log value is too large, assign it infinity
                posterior[label] = float('inf')

        sum_posterior = sum(posterior.values())
        for label in posterior:
            if posterior[label] == float('inf'):
                posterior[label] = 1.0
            else:
                posterior[label] /= sum_posterior
            posteriors.append(posterior.copy())
    return posteriors


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(cleaned_emails, labels, test_size=0.33, random_state=42)
#random_state gives the algorithm a seed to start at. Keeoing it fixed ensures the same split is obtained everytime

term_docs_train = cv.fit_transform(X_train)
label_index = get_label_index(Y_train)
prior = get_prior(label_index)
likelihood = get_likelihood(term_docs_train, label_index, smoothing)

term_docs_test = cv.transform(X_test)
posterior = get_posterior(term_docs_test, prior, likelihood)
#print(posterior)
#print(Y_test)
#Evaluation of models
correct = 0.0
for pred, actual in zip(posterior, Y_test):
    if actual == 1:
        if pred[1] >= 0.5:
            correct += 1
    elif pred[0] >= 0.5:
        correct += 1

acc = correct/len(Y_test)
print("The accuracy on {0} test samples is {1:0.1f}%".format(len(Y_test), acc*100))   

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB(alpha=1.0, fit_prior= True)
clf.fit(term_docs_train, Y_train)

prediction = clf.predict(term_docs_test)
prediction[:10]

accuracy = clf.score(term_docs_test, Y_test)
print("The accuracy using MultinomialNB is {0:.1f}%".format(accuracy*100))

#Precision-- How many are correct, Recall-- How many are correctly identified, F1 score is their harmonic mean
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report

precision = precision_score(Y_test, prediction, pos_label = 1)    #indicating test for spam i.e label 1
recall = recall_score(Y_test, prediction, pos_label = 1)
F1score = f1_score(Y_test, prediction, pos_label = 1)
print("Precision: {}  Recall: {}  F1 Score: {}".format(precision, recall,F1score))

#to find for all classes:
report = classification_report(Y_test, prediction)
print(report)









