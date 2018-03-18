from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import pickle

dataset = load_diabetes()
X, y = dataset.data, dataset.target
num_new = 30    #last 30 samples as training

X_train = X[:-num_new, :]
y_train = y[:-num_new]
X_test = X[-num_new:]
y_test= y[-num_new:]

scaler = StandardScaler()
scaler.fit(X_train)
pickle.dump(scaler, open('scaler.p', 'wb'))    #save the pickled, fitted scaler
X_scaled_train = scaler.transform(X_train)

regressor = SVR(C=20)
regressor.fit(X_scaled_train, y_train)
pickle.dump(regressor, open('regressor.p', 'wb'))

#In the deployment stage we load the saved scaler and regressor

my_scaler = pickle.load(open('scaler.p', 'rb'))
my_regressor = pickle.load(open('regressor.p', 'rb'))

#transform as it is already fitted to X_train
X_scaled_new = my_scaler.transform(X_test)
predictions = my_regressor.predict(X_scaled_new)
print(predictions)

