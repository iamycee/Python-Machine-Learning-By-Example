import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1.0 / (1 + np.exp(-z))

def compute_prediction(X, weights):
    """Get the prediction P(y=1|x) or P(y=0|x)"""
    z= np.dot(X, weights)    #get the weighted sum
    predictions = sigmoid(z)
    return predictions

def update_weights(X_train, y_train, weights, alpha):
    """updates weights as w := w + (alpha*dw)"""
    predictions = compute_prediction(X_train, weights)
    weights_delta = np.dot(X_train.T, y_train - predictions)    #vectorized implementation
    m = y_train.shape[0]
    weights += alpha / float(m) * weights_delta
    return weights    #returns updated weights

#now that we have the weight updation thing, lets calculate the cost
def compute_cost(X, y,  weights):
    """Computes the cost J(w)"""
    predictions = compute_prediction(X,weights)
    cost = np.mean(-y * np.log(predictions) - (1-y) *
                    np.log(1 - predictions))
    return cost

#this one returns weights for optimal cost
def train_logistic_regression(X_train, y_train, max_iter, alpha, fit_intercept= False):
    """alpha is the learning rate, fit intercept is the w0 added to the weighted sum"""
    if fit_intercept:
        intercept = np.ones((X_train.shape[0],1))
        X_train = np.hstack((intercept, X_train))    #stacks both arrays horizontally

    weights = np.zeros(X_train.shape[1])

    for iteration in range(max_iter):
        weights = update_weights(X_train, y_train, weights, alpha)
        #print cost every 100 iterations
        if iteration%100 == 0:
            print(compute_cost(X_train, y_train, weights))
    return weights    #returns the optimal weights

#predict results for new examples
def predict(X, weights):
    if X.shape[1] == weights.shape[0] - 1:    #if X is less
        intercept = np.ones((X.shape[0],1))     #add an intercept
        X = np.hstack((intercept,X))
    return compute_prediction(X,weights)

#Let's test this

X_train = np.array([[6,7],[2,4],[3,6],[4,7],[1,6],[5,2],[2,0],[6,3],[4,1],[7,2]])
y_train = np.array([0,0,0,0,0,1,1,1,1,1])

#train them weights  {weight training lol}
weights = train_logistic_regression(X_train, y_train, max_iter=1000, alpha=0.1, fit_intercept=True)
#tweak these parameters and see interesting results
plt.scatter(X_train[:,0], X_train[:,1], c=['b']*5+['k']*5, marker='o')    #plot the training data with 'o's


X_test = np.array([[6,1], [1,3], [3,1], [4,5]])
predictions = predict(X_test, weights)

#using 0.5 as the classification threshold

colors = ['k' if prediction >=0.5 else 'b' for prediction in predictions]
plt.scatter(X_test[:,0], X_test[:,1], marker='*', c=colors)
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()












