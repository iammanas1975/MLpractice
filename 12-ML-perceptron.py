X = []
Xtrain = []
Xtest = []
w = [0,0,0,0]
y = []
ytrain = []
ytest = []
animap = {'elephant':1, 'tiger':2, 'mouse':3}
iter = 10				#LEARNING - INCREASING NO. OF ITERATIONS CAN MAKE LEARNING BETTER (CONVERGE GRADUALLY)
eta = 0.05				#LEARNING - INCREASING ETA (LEARNING RATE) CAN MAKE LEARNING FASTER (CONVERGE FASTER)
errors = []

f = open('animals.txt')

def net_input(x):			#compute the input as function
	z = w[0] + w[1]*int(x[0]) + w[2]*int(x[1]) + w[3]*int(x[2])
	print('input function = %.2f' %(z,))	#debug print - to check values of input function to consider for prediction
					#LEARNING - DECIDING VALUE RANGES OF INPUT FUNCTIONS IS KEY TO PREDICT CATEGORIES CORRECTLY
					#LEARNING - SEE BELOW ON HOW IT IMPACTS THE LABELS (RESULTS) IN predict() FUNCTION
	return z

def predict(x):				#predict based on new set of data (x[])
	if net_input(x) < -40000.0:
		return 1
	elif net_input(x) < -5000.0:
		return 2
	else:
		return 3

for line in f:				#populate all data into an array
	arow = line.strip()
	parseline = arow.split('-')
	X.append(parseline[0:3])	#first 3 parameters are independent variables
	y.append(animap[parseline[3]])	#last parameter is known label (result or category to be predicted)
#print(X,'\n',y)			#debug print - check if data parsed from file

for i in range(20):			#create training data
	Xtrain.append(X[i])
	ytrain.append(y[i])
	#print(Xtrain[i],ytrain[i])	debug print - check if training data parsed well
for i in range(5):			#create test data
	Xtest.append(X[20+i])
	ytest.append(y[20+i])
for i in range(iter):			#learning algorithm - adjust weights
	err = 0
	for xi, target in zip(Xtrain, ytrain):
		update = eta * (target - predict(xi))	#better prediction -> lower weight changes -> controlled input function value ->
							# -> better prediction
		w[0] += update
		w[1] += update * int(xi[0])
		w[2] += update * int(xi[1])
		w[3] += update * int(xi[2])
		err += int(update != 0.0)
		print('update %.2f, weights [%.2f, %.2f, %.2f, %.2f], target %d, predicted %d, step %d' %(update, w[0], w[1], w[2], w[3], target, predict(xi),i)) 
		#print(update,': ',w,': ',predict(xi),': ',i)	#debug print - check adjustment of weights
	errors.append(err)
print('errors = ',errors)

for i in range(5):
	print(predict(Xtest[i]),' v/s ',ytest[i])

f.close()
