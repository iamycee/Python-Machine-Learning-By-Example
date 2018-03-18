import numpy as np
import matplotlib.pyplot as plt


def compute_predictions(X, weights):
    predictions = np.dot(X, weights)    #get weighted sum
    return predictions

def update_weights(X_train, y_train, weights, learning_rate):
    predictions = compute_predictions(X_train, weights)
    weights_delta = np.dot(X_train.T, y_train - predictions)
    m = y_train.shape[0]    #number of training samples
    weights += learning_rate/float(m) * weights_delta
    return weights

def compute_cost(X,y,weights):
    predictions = compute_predictions(X,weights)
    cost = np.mean((predictions - y)**2 / 2.0)    #mean squared cost
    return cost

def train_linear_regression(X_train, y_train, max_iter, learning_rate, fit_intercept=False):
    if fit_intercept:
        intercept = np.ones((X_train.shape[0], 1))
        X_train = np.hstack((intercept, X_train))
    weights = np.zeros(X_train.shape[1])
    for iteration in range(max_iter):
        weights = update_weights(X_train, y_train, weights, learning_rate)
        if iteration%100 == 0:
            print(compute_cost(X_train, y_train, weights))
    return weights

#these are the updated weights
def predict(X,weights):    #prediction for unlabelled data
    if X.shape[1] == weights.shape[0] - 1:
        intercept = np.ones((X.shape[0],1))
        X = np.hstack((intercept, X))
    return compute_predictions(X,weights)

X_train = np.array([[6], [2], [3], [4], [1],
            [5], [2], [6], [4], [7]])

y_train = np.array([5.5, 1.6, 2.2, 3.7, 0.8, 5.2, 1.5, 5.3, 4.4, 6.8])

weights = train_linear_regression(X_train, y_train, max_iter=100, learning_rate=0.01, fit_intercept=True)

X_test = np.array([[1.3], [3.5], [5.2], [2.8]])

predictions = predict(X_test, weights)

plt.scatter(X_train[:,0], y_train, marker='o', color='blue')
plt.plot(X_test[:,0], predictions, marker='*', color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.show()


from sklearn import datasets

diabetes = datasets.load_diabetes()
print(diabetes.data.shape)

num_test = 30    #last 30 samples are testing
X_train = diabetes.data[:-num_test]
y_train = diabetes.target[:-num_test]
#training
weights = train_linear_regression(X_train, y_train, max_iter=5000, learning_rate=1, fit_intercept=True)

X_test = diabetes.data[-num_test:]    #lasat 30
y_test = diabetes.target[-num_test:]

predictions = predict(X_test, weights)
print(predictions)  #this would be close to y_test

















