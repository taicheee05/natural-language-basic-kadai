import pandas as pd
import numpy as np
from sklearn import tree


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
