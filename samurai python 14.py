import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from prophet import Prophet
from prophet.diagnostics import cross_validation


df = pd.read_csv('https://raw.githubusercontent.com/facebook/prophet/main/examples/example_air_passengers.csv')
print(df.head())
time = pd.to_datetime(df['ds'])
sns.lineplot(x=time, y=df['y'])
print(df.info())

model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=36, freq='MS')
print(future)
forecast = model.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
fig_forecast = model.plot(forecast)
print(forecast.head())
