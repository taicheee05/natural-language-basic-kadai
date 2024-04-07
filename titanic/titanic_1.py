import pandas as pd
import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt
import seaborn as sns


# CSVファイルのパスを指定
file_path_1 = r'C:\Users\mt199\Dropbox\program\samurai\titanic\gender_submission.csv'
file_path_2 = r'C:\Users\mt199\Dropbox\program\samurai\titanic\test.csv'
file_path_3 = r'C:\Users\mt199\Dropbox\program\samurai\titanic\train.csv'

# CSVファイルを読み込む
df_1 = pd.read_csv(file_path_1)
df_test = pd.read_csv(file_path_2)
df_train = pd.read_csv(file_path_3)
# データフレームの内容を表示
# print(df_1.head(),df_1.shape)
# print(df_test.head(),df_test.shape)
df_train["Age"]=df_train['Age'].fillna(df_train['Age'].median())
df_train.replace({'male': 0,'female': 1} ,inplace=True)
print(df_train.head(),df_train.shape,df_train.isnull().sum())

train_features = df_train[['Pclass', 'Sex', 'Age', 'Fare']].values
train_target = df_train['Survived'].values

model = tree.DecisionTreeClassifier(max_depth = 5, class_weight = 'balanced', random_state=0)
model.fit(train_features, train_target)

df_test["Age"]=df_test['Age'].fillna(df_test['Age'].median())
df_test.replace({'male': 0,'female': 1} ,inplace=True)
df_test["Fare"] = df_test['Fare'].fillna(df_test['Fare'].median())
test_features = df_test[['Pclass', 'Sex', 'Age', 'Fare']].values
predict_test_target = model.predict(test_features)
print(predict_test_target)
submission = pd.DataFrame({'PassengerId': df_test['PassengerId'], 'Survived': predict_test_target})
submission.to_csv(r'C:\Users\mt199\Dropbox\program\samurai\titanic\submission_Titanic_DecisionTreeClassifier_1.csv', index = False )

print(df_train.describe())
print(df_test.describe())
df_train['Survived'] = df_train['Survived'].astype(str)
sns.countplot(x='Pclass', hue='Survived', data=df_train)
plt.show()