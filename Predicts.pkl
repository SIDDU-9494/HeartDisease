import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
dt=pd.read_csv('https://www.dropbox.com/s/ltksjtb54wrov5q/HeartDisease.csv?dl=1')
X=dt.drop('target',axis=1)
y=dt['target']
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.8,shuffle=True)
Model=LogisticRegression()
Model.fit(X_train,y_train)
predictions=Model.predict(X_test)
accuracy_score(y_test,predictions)
