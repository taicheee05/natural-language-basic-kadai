import pandas as pd
import seaborn as sns
from sklearn.datasets import fetch_california_housing
import japanize_matplotlib
import matplotlib.pyplot as plt


dataset = fetch_california_housing()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
print(dataset.DESCR)

df["price"]=dataset.target
feature_names_JPN = ['所得', '築年数', '部屋数', '寝室数', '地域人口', '世帯人数', '緯度', '経度', '住宅価格']
df.columns=feature_names_JPN
df=df[df["築年数"]!=52]
df=df[df['住宅価格']!=5.00001]
df['世帯数'] = df['地域人口']/df['世帯人数']
df['全部屋数'] = df['部屋数']*df['世帯数']
df['全寝室数'] = df['寝室数']*df['世帯数']
df['部屋数/人'] = df['全部屋数']/df['地域人口']
df['寝室数/人'] = df['全寝室数']/df['地域人口']
df=df.drop(columns=['部屋数','寝室数', '世帯人数', '世帯数', '全部屋数', '全寝室数'])
df.hist(figsize=(12, 10), bins=30)
df.to_csv(r'C:\Users\mt199\Dropbox\program\samurai\california_housing_cleansing.csv')


