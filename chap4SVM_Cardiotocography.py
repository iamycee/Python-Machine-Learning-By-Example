#Cardiotocography (CTG) is a technical means of recording
#the fetal heartbeat and the uterine contractions during pregnancy

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from collections import Counter
import timeit

df = pd.read_excel('CTG.xls', "Raw Data")
X = df.ix[1:2126, 3:-2].values  #third to 2nd last column has features
Y = df.ix[1:2126, -1].values    #last column has the labels NSP

print(Counter(Y))

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

svc = SVC(kernel='rbf')    #radial basis function
parameters = {'C': (100, 1e3, 1e4, 1e5), 'gamma': (1e-08, 1e-7, 1e-6, 1e-5)}

grid_search = GridSearchCV(svc, parameters, n_jobs=-1, cv=3)
start_time = timeit.default_timer()
grid_search.fit(X_train, Y_train)
print("--- %0.3f seconds" %(timeit.default_timer() - start_time))

#We can obtain the best parameter C by using
grid_search.best_params_

#We can obtain the best 30fold average performance under the optimal set of parameters:
grid_search.best_score_

#Retrieve the SVM model with the optimal parameter and apply it to the unknown testing set
svc_best = grid_search.best_estimator_

accuracy = svc_best.score(X_test, Y_test)
print("The accuracy on the testing set is : %.3f" %(accuracy*100))

prediction = svc_best.predict(X_test)
report = classification_report(Y_test, prediction)
print(report)












