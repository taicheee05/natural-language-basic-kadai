from sklearn.datasets import load_wine
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


dataset = load_wine()
df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
df["category"]=dataset.target
X=dataset.data
y=dataset.target
train_test_split(X, y, test_size=0.3, random_state=5)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5)

# ランダムフォレスト分類器のインスタンス化
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')t