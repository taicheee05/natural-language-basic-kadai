import numpy as np
import pandas as pd
import seaborn as sns
import japanize_matplotlib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib as plt
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r'C:\Users\mt199\Dropbox\program\samurai\california_housing_cleansing.csv')
df = df.drop(columns = ['Unnamed: 0'])
X=df.drop(columns=["住宅価格"]).to_numpy()
y=df["住宅価格"].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
print(X_train.shape,X_test.shape)
model = LinearRegression()

model.fit(X_train, y_train)

print(model.score(X_train, y_train))
print(model.score(X_test, y_test))

print(sns.barplot(x = ['所得', '築年数', '地域人口', '緯度', '経度', '部屋数/人', '寝室数/人'], y=model.coef_))

scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled=scaler.transform(X_train)

df_X_train=pd.DataFrame(X_train,columns=['所得', '築年数', '地域人口', '緯度', '経度', '部屋数', '寝室数'])
print(df_X_train.head())

df_X_train_scaled = pd.DataFrame(X_train_scaled, columns=['所得', '築年数', '地域人口', '緯度', '経度', '部屋数', '寝室数'])
print(df_X_train_scaled.head())

print(df_X_train_scaled.describe())

X_test_scaled=scaler.transform(X_test)
df_X_test = pd.DataFrame(X_test, columns=['所得', '築年数', '地域人口', '緯度', '経度', '部屋数', '寝室数'])
print(df_X_test.head())

df_X_test_scaled = pd.DataFrame(X_test_scaled, columns=['所得', '築年数', '地域人口', '緯度', '経度', '部屋数', '寝室数'])
print(df_X_test_scaled.head())

print(df_X_test_scaled.describe())


