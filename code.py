import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("C:\\Users\\HP\\Downloads\\mail_data.csv")
print(df.head)
data = df.where((pd.notnull(df)),'')

data.head(7)
data.info()
data.shape
data.loc[data['Category']=='spam', 'Category',]=0
data.loc[data['Category']=='ham', 'Category',]=1

X= data['Message']
Y= data['Category']
print(X)
print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size= 0.2, random_state=3)
print(X.shape)
print(X_train.shape)
print(X_test.shape)

feature_extraction= TfidfVectorizer(min_df= 1, stop_words='english', lowercase= 'true')

X_train_feature= feature_extraction.fit_transform(X_train)
X_test_feature= feature_extraction.transform(X_test)

Y_train = Y_train.astype('int')
Y_test= Y_test.astype('int')

print(X_train)
print(X_train_feature)

model= LogisticRegression()
model.fit(X_train_feature, Y_train)
prediction_on_training_data= model.predict(X_train_feature)
accuracy_on_training_data= accuracy_score(Y_train, prediction_on_training_data)

print('accuracy on train data :',accuracy_on_training_data)
prediction_on_test_data=  model.predict(X_test_feature)
accuracy_on_test_data= accuracy_score(Y_test, prediction_on_test_data)

print('accuracy on test data :',accuracy_on_test_data)

input_mail= [""]

input_data_features = feature_extraction.transform(input_mail) 

prediction= model.predict(input_data_features)

print(prediction)

if(prediction[0]==1):
    print('HAM mail')
else:
    print('SPAM mail')
