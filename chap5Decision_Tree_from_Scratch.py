import numpy as np


def gini_impurity(labels):
    #Empty set is pure set
    if labels.size == 0:
        return 0
    #Count the occurences of each label
    counts = np.unique(labels, return_counts=True)[1]
    fractions = counts / float(len(labels))
    return 1 - np.sum(fractions**2)

def entropy(labels):
    #Empty set is pure set
    if labels.size == 0:
        return 0
    counts = np.unique(labels, return_counts=True)[1]
    fractions = counts / float(len(labels))
    return -np.sum(fractions * np.log2(fractions))

#getting the weighted impurity <gini or entropy>
criterion_function = {'gini': gini_impurity, 'entropy': entropy}    #dict to choose function

def weighted_impurity(groups, criterion='gini'):
    #groups is 2 or more groups of children to evaluate default criterion is gini
    #returns the weighted impurity

    total = sum(len(group) for group in groups)
    weighted_sum = 0.0
    for group in groups:
        #key = frozenset(dict_key.items())
        #A frozenset is an immutable set
        #key = frozenset(criterion.items())
        #---this does not work for some reason: metric = criterion_function[criterion], so fixed it to gini for now
        metric = criterion_function['gini']    #gini_impurity function assigned to variable metric
        #print(metric(group))    #gini_impurity
        weighted_sum += len(group) / float(total) * metric(group)
        print(weighted_sum)

    return weighted_sum


#Spilt into left and right given a feature value
def split_node(X, y, index, value):
    """returns a list [X,y] with left and right nodes"""
    x_index = X[:,index]
    #if his feature is numerical
    if X[0, index].dtype.type in ['i','f']:    #int or float
        mask = x_index >= value    #true or false
    #if categorical
    else:
        mask = x_index == value    #true or false
    #split into left and right
    left = [X[~mask, :], y[~mask]]
    right = [X[mask, :], y[mask]]

    return left, right

#getting the best split by trying all possible splits and taking the best criterion
def get_best_split(X,y,criterion):
    best_index, best_value, best_score, children = None, None, 1, None
    for index in range(len(X[0])):    #try for every feature
        for value in  np.sort(np.unique(X[:,index])):
            groups = split_node(X, y, index, value)    #returns left, right
            impurity = weighted_impurity([groups[0][1], groups[1][1]], criterion)
            if impurity < best_score:
                best_index, best_value, best_score, children = index, value, impurity, groups
    return {'index': best_index, 'value': best_value, 'children': children}

def get_leaf(labels):
    #Obtain leaf as the majority of labels
    return np.bincount(labels).argmax()

#---RECURSIVE FUNCTION TO LINK ALL THESE TOGETHER---#
#1. Assign leaf if child nodes are empty
#2. Assign leaf if branch depth exceeds the depth allowed
#3. Assign  a leaf node if not enough samples for further split
#4. Keep splitting at the optimal point until these are met 

def split(node, max_depth, min_size, depth, criterion):
    #node is the dict get_best_split returns with children info
    left, right = node['children']
    del (node['children'])    #delete the node
    if left[1].size == 0:
        node['right'] = get_leaf(right[1])
        return
    if right[1].size == 0:
        node['left'] = get_leaf(left[1])
        return
    #Check if current depth is more than maximal depth
    if depth >= max_depth:
        node['left'], node['right'] = get_leaf(left[1]), get_leaf(right[1])
        return
    #Check if left child has enough samples
    if left[1].size <= min_size:
        node['left'] = get_leaf(left[1])
    else:
        #else it has enough samples so split it
        result = get_best_split(left[0], left[1], criterion)
        result_left, result_right = result['children']
        if result_left[1].size == 0:
            node['left'] = get_leaf(result_right[1])
        elif result_right[1].size == 0:
            node['left'] = get_leaf(result_left[1])
        else:
            node['left'] = result
            split(node['left'], max_depth, min_size ,depth+1, criterion)    #recursive call
            
    #Check if right child has enough samples
    if right[1].size <= min_size:
        node['right'] = get_leaf(right[1])
    else:
        #else it has enough samples so split it
        result = get_best_split(right[0], right[1], criterion)
        result_left, result_right = result['children']

        if result_left[1].size == 0:
            node['right'] = get_leaf(result_right[1])
        elif result_right[1].size == 0:
            node['right'] = get_leaf(result_left[1])
        else:
            node['right'] = result
            split(node['right'], max_depth, min_size, criterion)

#Tree construction, this the main function sorta
def train_tree(X_train, y_train, max_depth, min_size, depth=1, criterion='gini'):
    X = np.array(X_train)
    y = np.array(y_train)
    root = get_best_split(X, y, criterion)
    split(root, max_depth, min_size, 1, criterion_function)
    return root


#displaying the tree
#all caps for coonstants as per PEP8
CONDITION = {'numerical': {'yes': '>=', 'no': '<'}, 'categorical': {'yes': 'is', 'no': 'is not'}}

def visualize_tree(node, depth=0):
    if isinstance(node, dict):
        if node['value'].dtype.kind in ['i', 'f']:      #%i and %f int or float
            condition = CONDITION['numerical']    #condition is a dict
        else:
            condition = CONDITION['categorical']
        print('{}|- X{} {} {}'.format(depth * ' ', node['index'] + 1, condition['no'], node['value']))
        if 'left' in node:
            visualize_tree(node['left'], depth+1)

        print('{}|- X{} {} {}'.format(depth * ' ', node['index'] + 1, condition['yes'], node['value']))
        if 'right' in node:
            visualize_tree(node['right'], depth + 1)
    else:
        print('{}[{}]'.format(depth * ' ', node))


#Dataset
X_train = [['tech', 'professional'],
           ['fashion', 'student'],
           ['fashion','professional'],
           ['sports','student'],
           ['tech','student'],
           ['tech','retired'],
           ['sports','professional']]
y_train = [1, 0, 0, 0, 1, 0, 1]

#Training the tree
tree = train_tree(X_train, y_train, 2, 2, criterion = 'gini')
#visualizing the tree
visualize_tree(tree)            

    
        
        
                    
    
    















#X_train_n = [[6,7],[2,4],[7,2],[3,6],[4,7],[5,2],[1,6],[2,0],[6,3],[4,1]]
#y_train_n = [0,0,0,0,0,1,1,1,1,1]
