Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
Traceback (most recent call last):
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 139, in <module>
    tree = train_tree(X_train, y_train, 2, 2)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 126, in train_tree
    split(root, max_depth, min_size, 1, criterion_function)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 95, in split
    result = get_best_split(left[0], left[1], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 61, in get_best_split
    impurity = weighted_impurity([groups[0][1], groups[1][1]], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 34, in weighted_impurity
    weighted_sum += len(group) / float(total) * criterion_function[criterion](group)
TypeError: unhashable type: 'dict'
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
<function gini_impurity at 0x00000205C5510D08>
<function gini_impurity at 0x00000205C5510D08>
<function gini_impurity at 0x00000205C5510D08>
<function gini_impurity at 0x00000205C5510D08>
<function gini_impurity at 0x00000205C5510D08>
<function gini_impurity at 0x00000205C5510D08>
<function gini_impurity at 0x00000205C5510D08>
<function gini_impurity at 0x00000205C5510D08>
<function gini_impurity at 0x00000205C5510D08>
<function gini_impurity at 0x00000205C5510D08>
<function gini_impurity at 0x00000205C5510D08>
<function gini_impurity at 0x00000205C5510D08>
Traceback (most recent call last):
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 141, in <module>
    tree = train_tree(X_train, y_train, 2, 2)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 128, in train_tree
    split(root, max_depth, min_size, 1, criterion_function)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 97, in split
    result = get_best_split(left[0], left[1], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 63, in get_best_split
    impurity = weighted_impurity([groups[0][1], groups[1][1]], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 34, in weighted_impurity
    metric = criterion_function[criterion]
TypeError: unhashable type: 'dict'
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
<function gini_impurity at 0x000002852C592D08>
<function gini_impurity at 0x000002852C592D08>
<function gini_impurity at 0x000002852C592D08>
<function gini_impurity at 0x000002852C592D08>
<function gini_impurity at 0x000002852C592D08>
<function gini_impurity at 0x000002852C592D08>
<function gini_impurity at 0x000002852C592D08>
<function gini_impurity at 0x000002852C592D08>
<function gini_impurity at 0x000002852C592D08>
<function gini_impurity at 0x000002852C592D08>
<function gini_impurity at 0x000002852C592D08>
<function gini_impurity at 0x000002852C592D08>
Traceback (most recent call last):
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 141, in <module>
    tree = train_tree(X_train, y_train, 2, 2, criterion = 'gini')
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 128, in train_tree
    split(root, max_depth, min_size, 1, criterion_function)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 97, in split
    result = get_best_split(left[0], left[1], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 63, in get_best_split
    impurity = weighted_impurity([groups[0][1], groups[1][1]], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 34, in weighted_impurity
    metric = criterion_function[criterion]
TypeError: unhashable type: 'dict'
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
<function gini_impurity at 0x00000222FB432D08>
Traceback (most recent call last):
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 141, in <module>
    tree = train_tree(X_train, y_train, 2, 2, criterion = 'gini')
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 127, in train_tree
    root = get_best_split(X, y, criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 63, in get_best_split
    impurity = weighted_impurity([groups[0][1], groups[1][1]], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 36, in weighted_impurity
    weighted_sum += len(group) / float(total) * criterion_function[criterion][group]
TypeError: 'function' object is not subscriptable
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
<function gini_impurity at 0x0000022A0BB01D08>
Traceback (most recent call last):
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 141, in <module>
    tree = train_tree(X_train, y_train, 2, 2, criterion = 'gini')
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 127, in train_tree
    root = get_best_split(X, y, criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 63, in get_best_split
    impurity = weighted_impurity([groups[0][1], groups[1][1]], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 36, in weighted_impurity
    weighted_sum += len(group) / float(total) * criterion_function[criterion(group)]
TypeError: 'str' object is not callable
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
<function gini_impurity at 0x000002055E93FD90>
Traceback (most recent call last):
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 142, in <module>
    tree = train_tree(X_train, y_train, 2, 2, criterion = 'gini')
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 128, in train_tree
    root = get_best_split(X, y, criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 64, in get_best_split
    impurity = weighted_impurity([groups[0][1], groups[1][1]], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 37, in weighted_impurity
    weighted_sum += len(group) / float(total) * criterion_function[criterion(group)]
TypeError: 'str' object is not callable
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
<function gini_impurity at 0x0000021713680D08>
<function gini_impurity at 0x0000021713680D08>
<function gini_impurity at 0x0000021713680D08>
<function gini_impurity at 0x0000021713680D08>
<function gini_impurity at 0x0000021713680D08>
<function gini_impurity at 0x0000021713680D08>
<function gini_impurity at 0x0000021713680D08>
<function gini_impurity at 0x0000021713680D08>
<function gini_impurity at 0x0000021713680D08>
<function gini_impurity at 0x0000021713680D08>
<function gini_impurity at 0x0000021713680D08>
<function gini_impurity at 0x0000021713680D08>
Traceback (most recent call last):
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 141, in <module>
    tree = train_tree(X_train, y_train, 2, 2, criterion = 'gini')
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 128, in train_tree
    split(root, max_depth, min_size, 1, criterion_function)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 97, in split
    result = get_best_split(left[0], left[1], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 63, in get_best_split
    impurity = weighted_impurity([groups[0][1], groups[1][1]], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 34, in weighted_impurity
    metric = criterion_function[criterion]
TypeError: unhashable type: 'dict'
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
<function gini_impurity at 0x0000021386BE2D08>
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
<function gini_impurity at 0x00000273E4F70D08>
0.34285714285714286
<function gini_impurity at 0x00000273E4F70D08>
0.34285714285714286
<function gini_impurity at 0x00000273E4F70D08>
0.34285714285714286
<function gini_impurity at 0x00000273E4F70D08>
0.4857142857142857
<function gini_impurity at 0x00000273E4F70D08>
0.21428571428571427
<function gini_impurity at 0x00000273E4F70D08>
0.40476190476190477
<function gini_impurity at 0x00000273E4F70D08>
0.21428571428571427
<function gini_impurity at 0x00000273E4F70D08>
0.40476190476190477
<function gini_impurity at 0x00000273E4F70D08>
0.42857142857142855
<function gini_impurity at 0x00000273E4F70D08>
0.42857142857142855
<function gini_impurity at 0x00000273E4F70D08>
0.2857142857142857
<function gini_impurity at 0x00000273E4F70D08>
0.47619047619047616
<function gini_impurity at 0x00000273E4F70D08>
0.26666666666666666
<function gini_impurity at 0x00000273E4F70D08>
0.4666666666666667
<function gini_impurity at 0x00000273E4F70D08>
0.2
<function gini_impurity at 0x00000273E4F70D08>
0.4666666666666667
<function gini_impurity at 0x00000273E4F70D08>
0.26666666666666666
<function gini_impurity at 0x00000273E4F70D08>
0.26666666666666666
<function gini_impurity at 0x00000273E4F70D08>
0.30000000000000004
<function gini_impurity at 0x00000273E4F70D08>
0.30000000000000004
<function gini_impurity at 0x00000273E4F70D08>
0.26666666666666666
<function gini_impurity at 0x00000273E4F70D08>
0.4666666666666667
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
<function gini_impurity at 0x00000176AE640D08>
0.34285714285714286
<function gini_impurity at 0x00000176AE640D08>
0.34285714285714286
<function gini_impurity at 0x00000176AE640D08>
0.34285714285714286
<function gini_impurity at 0x00000176AE640D08>
0.4857142857142857
<function gini_impurity at 0x00000176AE640D08>
0.21428571428571427
<function gini_impurity at 0x00000176AE640D08>
0.40476190476190477
<function gini_impurity at 0x00000176AE640D08>
0.21428571428571427
<function gini_impurity at 0x00000176AE640D08>
0.40476190476190477
<function gini_impurity at 0x00000176AE640D08>
0.42857142857142855
<function gini_impurity at 0x00000176AE640D08>
0.42857142857142855
<function gini_impurity at 0x00000176AE640D08>
0.2857142857142857
<function gini_impurity at 0x00000176AE640D08>
0.47619047619047616
Traceback (most recent call last):
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 142, in <module>
    tree = train_tree(X_train, y_train, 2, 2, criterion = 'gini')
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 129, in train_tree
    split(root, max_depth, min_size, 1, criterion_function)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 98, in split
    result = get_best_split(left[0], left[1], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 64, in get_best_split
    impurity = weighted_impurity([groups[0][1], groups[1][1]], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 34, in weighted_impurity
    metric = criterion_function[criterion]
TypeError: unhashable type: 'dict'
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
Traceback (most recent call last):
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 143, in <module>
    tree = train_tree(X_train, y_train, 2, 2, criterion = 'gini')
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 129, in train_tree
    split(root, max_depth, min_size, 1, criterion_function)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 98, in split
    result = get_best_split(left[0], left[1], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 64, in get_best_split
    impurity = weighted_impurity([groups[0][1], groups[1][1]], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 34, in weighted_impurity
    metric = criterion_function[criterion]
TypeError: unhashable type: 'dict'
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
0.34285714285714286
0.34285714285714286
0.34285714285714286
0.4857142857142857
0.21428571428571427
0.40476190476190477
0.21428571428571427
0.40476190476190477
0.42857142857142855
0.42857142857142855
0.2857142857142857
0.47619047619047616
Traceback (most recent call last):
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 143, in <module>
    tree = train_tree(X_train, y_train, 2, 2, criterion = 'gini')
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 129, in train_tree
    split(root, max_depth, min_size, 1, criterion_function)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 98, in split
    result = get_best_split(left[0], left[1], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 64, in get_best_split
    impurity = weighted_impurity([groups[0][1], groups[1][1]], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 34, in weighted_impurity
    metric = criterion_function[criterion]
TypeError: unhashable type: 'dict'
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
0.48
0.34285714285714286
0.0
0.34285714285714286
0.48
0.34285714285714286
0.5
0.4857142857142857
0.375
0.21428571428571427
0.4444444444444444
0.40476190476190477
0.375
0.21428571428571427
0.4444444444444444
0.40476190476190477
0.5
0.42857142857142855
0.0
0.42857142857142855
0.5
0.2857142857142857
0.4444444444444444
0.47619047619047616
Traceback (most recent call last):
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 143, in <module>
    tree = train_tree(X_train, y_train, 2, 2, criterion = 'gini')
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 129, in train_tree
    split(root, max_depth, min_size, 1, criterion_function)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 98, in split
    result = get_best_split(left[0], left[1], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 64, in get_best_split
    impurity = weighted_impurity([groups[0][1], groups[1][1]], criterion)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 34, in weighted_impurity
    metric = criterion_function[criterion]
TypeError: unhashable type: 'dict'
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
0.34285714285714286
0.34285714285714286
0.34285714285714286
0.4857142857142857
0.21428571428571427
0.40476190476190477
0.21428571428571427
0.40476190476190477
0.42857142857142855
0.42857142857142855
0.2857142857142857
0.47619047619047616
0.26666666666666666
0.4666666666666667
0.2
0.4666666666666667
0.26666666666666666
0.26666666666666666
0.30000000000000004
0.30000000000000004
0.26666666666666666
0.4666666666666667
Traceback (most recent call last):
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 163, in <module>
    visualize_tree(tree)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 154, in visualize_tree
    condition = COCNDITION['categorical']
NameError: name 'COCNDITION' is not defined
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
0.34285714285714286
0.34285714285714286
0.34285714285714286
0.4857142857142857
0.21428571428571427
0.40476190476190477
0.21428571428571427
0.40476190476190477
0.42857142857142855
0.42857142857142855
0.2857142857142857
0.47619047619047616
0.26666666666666666
0.4666666666666667
0.2
0.4666666666666667
0.26666666666666666
0.26666666666666666
0.30000000000000004
0.30000000000000004
0.26666666666666666
0.4666666666666667
Traceback (most recent call last):
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 164, in <module>
    visualize_tree(tree)
  File "C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py", line 155, in visualize_tree
    condition = COCNDITION['categorical']
NameError: name 'COCNDITION' is not defined
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
0.34285714285714286
0.34285714285714286
0.34285714285714286
0.4857142857142857
0.21428571428571427
0.40476190476190477
0.21428571428571427
0.40476190476190477
0.42857142857142855
0.42857142857142855
0.2857142857142857
0.47619047619047616
0.26666666666666666
0.4666666666666667
0.2
0.4666666666666667
0.26666666666666666
0.26666666666666666
0.30000000000000004
0.30000000000000004
0.26666666666666666
0.4666666666666667
|- X1 is not fashion
 |- X2 is not professional
 |- X2 is professional
|- X1 is fashion
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
0.34285714285714286
0.34285714285714286
0.34285714285714286
0.4857142857142857
0.21428571428571427
0.40476190476190477
0.21428571428571427
0.40476190476190477
0.42857142857142855
0.42857142857142855
0.2857142857142857
0.47619047619047616
0.26666666666666666
0.4666666666666667
0.2
0.4666666666666667
0.26666666666666666
0.26666666666666666
0.30000000000000004
0.30000000000000004
0.26666666666666666
0.4666666666666667
|- X1 is not fashion
 |- X2 is not professional
  [0]
 |- X2 is professional
  [1]
|- X1 is fashion
 [0]
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
0.34285714285714286
0.34285714285714286
0.34285714285714286
0.4857142857142857
0.21428571428571427
0.40476190476190477
0.21428571428571427
0.40476190476190477
0.42857142857142855
0.42857142857142855
0.2857142857142857
0.47619047619047616
0.26666666666666666
0.4666666666666667
0.2
0.4666666666666667
0.26666666666666666
0.26666666666666666
0.30000000000000004
0.30000000000000004
0.26666666666666666
0.4666666666666667
|- X1 is not fashion
 |- X2 is not professional
  [0]
 |- X2 is professional
  [1]
|- X1 is fashion
 [0]
>>> 
 RESTART: C:\Stuff\Programming\PythonML\PythonML_book\chap5Decision_Tree_from_Scratch.py 
0.34285714285714286
0.34285714285714286
0.34285714285714286
0.4857142857142857
0.21428571428571427
0.40476190476190477
0.21428571428571427
0.40476190476190477
0.42857142857142855
0.42857142857142855
0.2857142857142857
0.47619047619047616
0.26666666666666666
0.4666666666666667
0.2
0.4666666666666667
0.26666666666666666
0.26666666666666666
0.30000000000000004
0.30000000000000004
0.26666666666666666
0.4666666666666667
|- X1 is not fashion
 |- X2 is not professional
  [0]
 |- X2 is professional
  [1]
|- X1 is fashion
 [0]
>>> visualize_tree(tree)
|- X1 is not fashion
 |- X2 is not professional
  [0]
 |- X2 is professional
  [1]
|- X1 is fashion
 [0]
>>> X
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    X
NameError: name 'X' is not defined
>>> X_train_num = [[6,7], [2,4]]
>>> X_train_num = [[6,7], [2,4]]
>>> X_train_num = [[6,7],[2,4],[7,2],[3,6],[4,7],[5,2],[1,6],[2,0],[6,3],[4,1]]
>>> y_train_num = [0,0,0,0,0,1,1,1,1,1]
>>> tree = train_tree(X_train_num, y)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tree = train_tree(X_train_num, y)
NameError: name 'y' is not defined
>>> tree = train_tree(X_train_num, y_train_num, 2, 2)
0.4444444444444444
0.4444444444444444
0.4
0.5
0.4444444444444444
0.4444444444444444
0.4
0.5
0.4444444444444444
0.4444444444444444
0.4
0.5
0.4444444444444444
0.4444444444444444
0.4444444444444444
0.4444444444444444
0.4444444444444444
0.4444444444444444
0.4
0.5
0.4444444444444444
0.4444444444444444
0.4444444444444444
0.4444444444444444
0.4
0.5
0.375
0.375
0.42857142857142866
0.42857142857142866
0.3333333333333333
0.4583333333333333
0.35714285714285715
0.35714285714285715
0.42857142857142866
0.42857142857142866
0.42857142857142866
0.42857142857142866
0.42857142857142866
0.42857142857142866
0.35714285714285715
0.35714285714285715
0.42857142857142866
0.42857142857142866
0.42857142857142866
0.42857142857142866
0.3333333333333333
0.4583333333333333
0.42857142857142866
0.42857142857142866
0.35714285714285715
0.35714285714285715
0.3333333333333333
0.4583333333333333
>>> visualize_tree(tree)
|- X2 < 7
 |- X1 < 3
  [1]
 |- X1 >= 3
  [0]
|- X2 >= 7
 [0]
>>> 
>>> 
>>> 
>>> help(time)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    help(time)
NameError: name 'time' is not defined
>>> import time
>>> import timeit
>>> help(time)
Help on built-in module time:

NAME
    time - This module provides various functions to manipulate time values.

DESCRIPTION
    There are two standard representations of time.  One is the number
    of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
    or a floating point number (to represent fractions of seconds).
    The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
    The actual value can be retrieved by calling gmtime(0).
    
    The other representation is a tuple of 9 integers giving local time.
    The tuple items are:
      year (including century, e.g. 1998)
      month (1-12)
      day (1-31)
      hours (0-23)
      minutes (0-59)
      seconds (0-59)
      weekday (0-6, Monday is 0)
      Julian day (day in the year, 1-366)
      DST (Daylight Savings Time) flag (-1, 0 or 1)
    If the DST flag is 0, the time is given in the regular time zone;
    if it is 1, the time is given in the DST time zone;
    if it is -1, mktime() should guess based on the date and time.
    
    Variables:
    
    timezone -- difference in seconds between UTC and local standard time
    altzone -- difference in  seconds between UTC and local DST time
    daylight -- whether local time should reflect DST
    tzname -- tuple of (standard time zone name, DST time zone name)
    
    Functions:
    
    time() -- return current time in seconds since the Epoch as a float
    clock() -- return CPU time since process start as a float
    sleep() -- delay for a number of seconds given as a float
    gmtime() -- convert seconds since Epoch to UTC tuple
    localtime() -- convert seconds since Epoch to local time tuple
    asctime() -- convert time tuple to string
    ctime() -- convert time in seconds to string
    mktime() -- convert local time tuple to seconds since Epoch
    strftime() -- convert time tuple to string according to format specification
    strptime() -- parse string to time tuple according to format specification
    tzset() -- change the local timezone

CLASSES
    builtins.tuple(builtins.object)
        struct_time
    
    class struct_time(builtins.tuple)
     |  The time value as returned by gmtime(), localtime(), and strptime(), and
     |  accepted by asctime(), mktime() and strftime().  May be considered as a
     |  sequence of 9 integers.
     |  
     |  Note that several fields' values are not the same as those defined by
     |  the C language standard for struct tm.  For example, the value of the
     |  field tm_year is the actual year, not year - 1900.  See individual
     |  fields' descriptions for details.
     |  
     |  Method resolution order:
     |      struct_time
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  tm_gmtoff
     |      offset from UTC in seconds
     |  
     |  tm_hour
     |      hours, range [0, 23]
     |  
     |  tm_isdst
     |      1 if summer time is in effect, 0 if not, and -1 if unknown
     |  
     |  tm_mday
     |      day of month, range [1, 31]
     |  
     |  tm_min
     |      minutes, range [0, 59]
     |  
     |  tm_mon
     |      month of year, range [1, 12]
     |  
     |  tm_sec
     |      seconds, range [0, 61])
     |  
     |  tm_wday
     |      day of week, range [0, 6], Monday is 0
     |  
     |  tm_yday
     |      day of year, range [1, 366]
     |  
     |  tm_year
     |      year, for example, 1993
     |  
     |  tm_zone
     |      abbreviation of timezone name
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  n_fields = 11
     |  
     |  n_sequence_fields = 9
     |  
     |  n_unnamed_fields = 0
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  count(...)
     |      T.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.

FUNCTIONS
    asctime(...)
        asctime([tuple]) -> string
        
        Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
        When the time tuple is not present, current time as returned by localtime()
        is used.
    
    clock(...)
        clock() -> floating point number
        
        Return the CPU time or real time since the start of the process or since
        the first call to clock().  This has as much precision as the system
        records.
    
    ctime(...)
        ctime(seconds) -> string
        
        Convert a time in seconds since the Epoch to a string in local time.
        This is equivalent to asctime(localtime(seconds)). When the time tuple is
        not present, current time as returned by localtime() is used.
    
    get_clock_info(...)
        get_clock_info(name: str) -> dict
        
        Get information of the specified clock.
    
    gmtime(...)
        gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                               tm_sec, tm_wday, tm_yday, tm_isdst)
        
        Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
        GMT).  When 'seconds' is not passed in, convert the current time instead.
        
        If the platform supports the tm_gmtoff and tm_zone, they are available as
        attributes only.
    
    localtime(...)
        localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                                  tm_sec,tm_wday,tm_yday,tm_isdst)
        
        Convert seconds since the Epoch to a time tuple expressing local time.
        When 'seconds' is not passed in, convert the current time instead.
    
    mktime(...)
        mktime(tuple) -> floating point number
        
        Convert a time tuple in local time to seconds since the Epoch.
        Note that mktime(gmtime(0)) will not generally return zero for most
        time zones; instead the returned value will either be equal to that
        of the timezone or altzone attributes on the time module.
    
    monotonic(...)
        monotonic() -> float
        
        Monotonic clock, cannot go backward.
    
    perf_counter(...)
        perf_counter() -> float
        
        Performance counter for benchmarking.
    
    process_time(...)
        process_time() -> float
        
        Process time for profiling: sum of the kernel and user-space CPU time.
    
    sleep(...)
        sleep(seconds)
        
        Delay execution for a given number of seconds.  The argument may be
        a floating point number for subsecond precision.
    
    strftime(...)
        strftime(format[, tuple]) -> string
        
        Convert a time tuple to a string according to a format specification.
        See the library reference manual for formatting codes. When the time tuple
        is not present, current time as returned by localtime() is used.
        
        Commonly used format codes:
        
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        
        Other codes may be available on your platform.  See documentation for
        the C library strftime function.
    
    strptime(...)
        strptime(string, format) -> struct_time
        
        Parse a string to a time tuple according to a format specification.
        See the library reference manual for formatting codes (same as
        strftime()).
        
        Commonly used format codes:
        
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        
        Other codes may be available on your platform.  See documentation for
        the C library strftime function.
    
    time(...)
        time() -> floating point number
        
        Return the current time in seconds since the Epoch.
        Fractions of a second may be present if the system clock provides them.

DATA
    altzone = -23400
    daylight = 0
    timezone = -19800
    tzname = ('India Standard Time', 'India Daylight Time')

FILE
    (built-in)


>>> help(timeit)
Help on module timeit:

NAME
    timeit - Tool for measuring execution time of small code snippets.

DESCRIPTION
    This module avoids a number of common traps for measuring execution
    times.  See also Tim Peters' introduction to the Algorithms chapter in
    the Python Cookbook, published by O'Reilly.
    
    Library usage: see the Timer class.
    
    Command line usage:
        python timeit.py [-n N] [-r N] [-s S] [-t] [-c] [-p] [-h] [--] [statement]
    
    Options:
      -n/--number N: how many times to execute 'statement' (default: see below)
      -r/--repeat N: how many times to repeat the timer (default 3)
      -s/--setup S: statement to be executed once initially (default 'pass').
                    Execution time of this setup statement is NOT timed.
      -p/--process: use time.process_time() (default is time.perf_counter())
      -t/--time: use time.time() (deprecated)
      -c/--clock: use time.clock() (deprecated)
      -v/--verbose: print raw timing results; repeat for more digits precision
      -u/--unit: set the output time unit (usec, msec, or sec)
      -h/--help: print this usage message and exit
      --: separate options from statement, use when statement starts with -
      statement: statement to be timed (default 'pass')
    
    A multi-line statement may be given by specifying each line as a
    separate argument; indented lines are possible by enclosing an
    argument in quotes and using leading spaces.  Multiple -s options are
    treated similarly.
    
    If -n is not given, a suitable number of loops is calculated by trying
    successive powers of 10 until the total time is at least 0.2 seconds.
    
    Note: there is a certain baseline overhead associated with executing a
    pass statement.  It differs between versions.  The code here doesn't try
    to hide it, but you should be aware of it.  The baseline overhead can be
    measured by invoking the program without arguments.
    
    Classes:
    
        Timer
    
    Functions:
    
        timeit(string, string) -> float
        repeat(string, string) -> list
        default_timer() -> float

CLASSES
    builtins.object
        Timer
    
    class Timer(builtins.object)
     |  Class for timing execution speed of small code snippets.
     |  
     |  The constructor takes a statement to be timed, an additional
     |  statement used for setup, and a timer function.  Both statements
     |  default to 'pass'; the timer function is platform-dependent (see
     |  module doc string).  If 'globals' is specified, the code will be
     |  executed within that namespace (as opposed to inside timeit's
     |  namespace).
     |  
     |  To measure the execution time of the first statement, use the
     |  timeit() method.  The repeat() method is a convenience to call
     |  timeit() multiple times and return a list of results.
     |  
     |  The statements may contain newlines, as long as they don't contain
     |  multi-line string literals.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, stmt='pass', setup='pass', timer=<built-in function perf_counter>, globals=None)
     |      Constructor.  See class doc string.
     |  
     |  autorange(self, callback=None)
     |      Return the number of loops and time taken so that total time >= 0.2.
     |      
     |      Calls the timeit method with *number* set to successive powers of
     |      ten (10, 100, 1000, ...) up to a maximum of one billion, until
     |      the time taken is at least 0.2 second, or the maximum is reached.
     |      Returns ``(number, time_taken)``.
     |      
     |      If *callback* is given and is not None, it will be called after
     |      each trial with two arguments: ``callback(number, time_taken)``.
     |  
     |  print_exc(self, file=None)
     |      Helper to print a traceback from the timed code.
     |      
     |      Typical use:
     |      
     |          t = Timer(...)       # outside the try/except
     |          try:
     |              t.timeit(...)    # or t.repeat(...)
     |          except:
     |              t.print_exc()
     |      
     |      The advantage over the standard traceback is that source lines
     |      in the compiled template will be displayed.
     |      
     |      The optional file argument directs where the traceback is
     |      sent; it defaults to sys.stderr.
     |  
     |  repeat(self, repeat=3, number=1000000)
     |      Call timeit() a few times.
     |      
     |      This is a convenience function that calls the timeit()
     |      repeatedly, returning a list of results.  The first argument
     |      specifies how many times to call timeit(), defaulting to 3;
     |      the second argument specifies the timer argument, defaulting
     |      to one million.
     |      
     |      Note: it's tempting to calculate mean and standard deviation
     |      from the result vector and report these.  However, this is not
     |      very useful.  In a typical case, the lowest value gives a
     |      lower bound for how fast your machine can run the given code
     |      snippet; higher values in the result vector are typically not
     |      caused by variability in Python's speed, but by other
     |      processes interfering with your timing accuracy.  So the min()
     |      of the result is probably the only number you should be
     |      interested in.  After that, you should look at the entire
     |      vector and apply common sense rather than statistics.
     |  
     |  timeit(self, number=1000000)
     |      Time 'number' executions of the main statement.
     |      
     |      To be precise, this executes the setup statement once, and
     |      then returns the time it takes to execute the main statement
     |      a number of times, as a float measured in seconds.  The
     |      argument is the number of times through the loop, defaulting
     |      to one million.  The main statement, the setup statement and
     |      the timer function to be used are passed to the constructor.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    default_timer = perf_counter(...)
        perf_counter() -> float
        
        Performance counter for benchmarking.
    
    repeat(stmt='pass', setup='pass', timer=<built-in function perf_counter>, repeat=3, number=1000000, globals=None)
        Convenience function to create Timer object and call repeat method.
    
    timeit(stmt='pass', setup='pass', timer=<built-in function perf_counter>, number=1000000, globals=None)
        Convenience function to create Timer object and call timeit method.

DATA
    __all__ = ['Timer', 'timeit', 'repeat', 'default_timer']

FILE
    c:\users\yc\appdata\local\programs\python\python36\lib\timeit.py


>>> 
>>> 
>>> 
>>> 
>>> dictX = {'age': 44, 'sex': male}
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dictX = {'age': 44, 'sex': male}
NameError: name 'male' is not defined
>>> dictX = {'age': 44, 'sex': 'male'}
>>> dictY = {'name': 'GiriVee', 'skl': 'none'}
>>> dictY
{'name': 'GiriVee', 'skl': 'none'}
>>> dictY.items()
dict_items([('name', 'GiriVee'), ('skl', 'none')])
>>> dictY['name']
'GiriVee'
>>> dictY[dictX]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dictY[dictX]
TypeError: unhashable type: 'dict'
>>> dictX.append('val':'name')
SyntaxError: invalid syntax
>>> dictX.append({'val':'name'})
