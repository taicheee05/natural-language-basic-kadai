import pandas as pd
import matplotlib.pyplot as plt
#pip install japanize-matplotlibはターミナルで実行
import japanize_matplotlib as jp_plt
df=pd.read_csv(r"C:\Users\mt199\Dropbox\program\samurai\sample_pandas_6.csv")
print(df['商品番号'].value_counts())
for column in df.columns:
    counts=df[column].value_counts()
    counts.plot(kind='bar')
    plt.title(f'{column}の出現頻度')
    plt.xlabel(column)
    plt.ylabel('頻度')
    plt.show()

print(df.groupby("商品番号")["単価"].sum())
print(df.groupby('商品番号')['単価'].describe())

