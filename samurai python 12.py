import pandas as pd
from sklearn.datasets import load_breast_cancer
import matplotlib as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import numpy as np
from sklearn.tree import export_text



dataset = load_breast_cancer()

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df['class'] = dataset.target
print(df.head())
print(df.columns)

X=df.drop(columns=['class']).to_numpy()
y=df['class'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

model = DecisionTreeClassifier(random_state=0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

df_X_new = pd.read_csv(r'C:\Users\mt199\Dropbox\program\samurai\data_breastcancer.csv')
df_X_new.head()
X_new = df_X_new.to_numpy()
model.predict(X_new)
