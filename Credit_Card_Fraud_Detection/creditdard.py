import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('D:\sjk10\Machine_learning\Credit_Card_Fraud_Detection\creditcard.csv')
#print(data.head())

count_classes = pd.value_counts(data['Class'], sort= True). sort_index()
count_classes.plot(kind = 'bar')
plt.title("Fraud class histogram")
plt.xlabel("Class")
plt.ylabel("Frequency")
#plt.show()

from sklearn.preprocessing import StandardScaler

data['normAmount'] = StandardScaler().fit_transform(data['Amount'].values.reshape(-1, 1))
data = data.drop(['Time','Amount'],axis=1)
data.head()

X = data.loc[:, data.columns !='Class']
y = data.loc[:, data.columns =='Class']

number_records_fraud = len(data[data.Class == 1]) #
fraud_indices = np.array(data[data.Class == 1].index)

normal_indices = data[data.Class == 0].index

random_normal_indices = np.random.choice(normal_indices, number_records_fraud, replace = False)
random_normal_indices = np.array(random_normal_indices)

under_sample_indices = np.concatenate([fraud_indices,random_normal_indices])

under_sample_data = data.iloc[under_sample_indices, :]

X_undersample = under_sample_data.loc[:, under_sample_data.columns != 'Class']
y_undersample = under_sample_data.loc[:, under_sample_data.columns == 'Class']

print("Percentage of normal transactions:", len(under_sample_data[under_sample_data.Class == 0])/len(under_sample_data))
print("Percentage of fraud transactions:", len(under_sample_data[under_sample_data.Class == 1])/len(under_sample_data))
print("Total number of transactions in resampled data: ", len(under_sample_data))

from sklearn.model_selection import train_test_split

X_train,X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

print("Number transactions train dataset:", len(X_train))
print("Number transactions test dataset: ", len(X_test))
print("Total number of transactions: ", len(X_train)+len(X_test))

X_train_undersample, X_test_undersample, y_train_undersample, y_test_undersample = train_test_split(X_undersample,y_undersample,test_size=0.3,random_state=0)

print("")
print("Number transactions train dataset:", len(X_train_undersample))
print("Number transactions test dataset: ", len(X_test_undersample))
print("Total number of transactions: ", len(X_train_undersample)+len(X_test_undersample))

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import confusion_matrix,recall_score,classification_report

def printing_KFold_scores(X_train_data, y_train_data):
	kf = KFold(5, shuffle=False)

	# Different C parameters
	c_param_range = [0.01, 0.1, 1, 10, 100]

	result_table = pd.DataFrame(index=range(len(c_param_range), 2), columns=['C_parameter', 'Mean recall score'])
	result_table['C_parameter'] = c_param_range

	# the k-fold will give 2 lists: train_indices = indices[0], test_indices = indices[1]
	j = 0
	for c_param in c_param_range:
		print("--------------------------------------------------")
		print("C parameter: ", c_param)
		print("--------------------------------------------------")
		print("")

		result_accs = []
		for iteration, indices in enumerate(kf.split(X_train_data)): 

			lr = LogisticRegression(C=c_param, penalty='l1',solver='liblinear')

			# Use the training data to fit the model. In this case, we use the portion of the fold to train the model
			# with indices[0]. We then predict on the portion assigned as the test cross validation with indices[1]
			lr.fit(X_train_data.iloc[indices[0], :], y_train_data.iloc[indices[0], :].values.ravel())

			# Predict values using the test indices in the training data
			Y_pred_undersample = lr.predict(X_train_data.iloc[indices[1], :].values)

			# Calculate the recall score and append it to a list for recall scores representing the current c_parameter
			recall_acc = recall_score(y_train_data.iloc[indices[1], :].values, Y_pred_undersample)
			result_accs.append(recall_acc)
			print('Iteration', iteration, ': recall score = ', recall_acc)

		# The mean value of those recall scores in the metric we want to save and get hold of.
		result_table.loc[j, 'Mean recall score'] = np.mean(result_accs)
		j += 1
		print("")
		print("Mean recall score: ", np.mean(result_accs))
		print("")

#	result_table['Mean recall score'] = result_table['Mean recall score'].astype('float64')
#	best_c = result_table.loc[result_table['Mean recall score'].idxmax()]['C_parameter']
	best_c = result_table.loc[result_table['Mean recall score'].astype('float32').idxmax()]['C_parameter']
	# Finally, we can check with C parameter is the best among the chosen
	print("********************************************************************************")
	print("Best model to choose from cross validation is with C parameter = ", best_c)
	print("********************************************************************************")

	return best_c

best_c = printing_KFold_scores(X_train_undersample,y_train_undersample)