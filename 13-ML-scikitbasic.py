#A LIST OF SUPERVISED LEARNING CLASSIFIERS AS PART OF SCIKIT LEARN IS INCLUDED

#IMPORT IRIS DATASET
"""
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
X = iris.data[:,[2,3]]		#pick up features (columns) 3rd & 4th
y = iris.target
#print(X,y)			#debug print

"""
#READ DATA FROM ANIMAL FILE
animap = {'elephant':1, 'tiger':2, 'mouse':3}
X = []				#in this case we are using lists instead of numpy
y = []
f = open('animals.txt')
for line in f:
	arow = line.strip()
	parseline = arow.split('-')
	X.append(parseline[0:3])
	y.append(animap[parseline[3]])

#SPLIT INTO TRAINING AND TEST DATA
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

#USE FEATURE SCALING
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

#NOW APPLY THE MODEL OF CHOICE: MODEL 1
from sklearn.linear_model import Perceptron
ppn = Perceptron(max_iter = 80, eta0 = 0.1, random_state = 0)
ppn.fit(X_train_std, y_train)

#NOW ARE THE PREDICTIONS!
y_pred = ppn.predict(X_test_std)
print('Misclassified examples: %d' % (y_test != y_pred).sum())
for a, b in zip(y_test, y_pred):
	print('y_test = %d and y_pred = %d' % (a, b))

#MODEL 2 - decreasing C increases regularization, increasing may lead to overfitting
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C = 1, random_state = 0)
lr.fit(X_train_std, y_train)
y_pred = lr.predict(X_test_std)
print('Misclassified examples: %d' % (y_test != y_pred).sum())
for a, b in zip(y_test, y_pred):
	print('y_test = %d and y_pred = %d' % (a, b))
print("Probability for 1st sample is ", lr.predict_proba(X_test_std[0,:].reshape(1,-1)))	#probability for 1st sample

#MODEL 3
from sklearn.svm import SVC
sv = SVC(kernel = 'linear', C = 1, random_state = 0)
sv.fit(X_train_std, y_train)
y_pred = sv.predict(X_test_std)
print('Misclassified examples: %d' % (y_test != y_pred).sum())
for a, b in zip(y_test, y_pred):
	print('y_test = %d and y_pred = %d' % (a, b))

#MODEL 4 - support vector machine (SVM) for non-linearly separable classes (RBF kernal projecting features to different dimension)
#sv = SVC(kernel = 'RBF', C = 1, random_state = 0)

#MODEL 5 - decision tree to phase wise select features and decide; max_depth is till what level the tree will run
#from sklearn.tree import DecisionTreeClassifier
#tree = DecisionTreeClassifier(criterion = 'entropy', max_depth = 3, random_stare = 0)

#MODEL 6 - random forest as ensemble of decision trees; estimators - no. of trees, jobs - no. of CPU cores to use)
#from sklearn.ensemble import RamdomForestClassifier
#forest = RandomForestClassifier(criterion = 'entropy', n_estimators = 10, random_state = 1, n_jobs = 2)

#MODEL 7 - KNN (K Nearest Neighbors); neighbors - no. of nearest samples within certain distance (given as metric + p parameters)
#from sklearn.neighbors import KNeighborsClassifier
#knn = KNeighborsClassifier(n_neighbors = 5, p = 2, metric = 'minkowski')
