import pandas as pd
import seaborn as sns
import japanize_matplotlib
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\mt199\Dropbox\program\samurai\california_housing_cleansing.csv')
df=df.drop(columns=['Unnamed: 0'])
scaler = StandardScaler()
X=df.to_numpy()
scaler.fit(X)
X_scaled=scaler.transform(X)
print(X_scaled)
model = KMeans(n_clusters=4, random_state=0)
model.fit(X_scaled)
print(df.head())
df["クラスター"]=model.labels_
print(df.head())
print(df.groupby('クラスター').mean())
df_cluster3 = df.query('クラスター == 3')
sns.scatterplot(x='経度', y='緯度', data=df_cluster3)
plt.show()
