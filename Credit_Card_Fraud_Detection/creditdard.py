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
Y = data.loc[:, data.columns =='Class']

number_records_fraud = len(data[data.Class == 1])
fraud_indices = np.array(data[data.Class == 1].index)

normal_indices = data[data.Class == 0].index

random_normal_indices = np.random.choice(normal_indices, number_records_fraud, replace = False)
random_normal_indices = np.array(random_normal_indices)

under_sample_indices = np.concatenate([fraud_indices,random_normal_indices])

under_sample_data = data.iloc[under_sample_indices, :]