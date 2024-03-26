import tensorflow as tf
from tensorflow.keras import utils
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense, Input
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt

utils.set_random_seed(0)
data = tf.keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = data
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
print(np.amin(x_train), np.amax(x_train))
print(np.amin(y_train), np.amax(y_train))
print(np.amin(x_test), np.amax(x_test))
print(np.amin(y_test), np.amax(y_test))
print(x_train[2])
plt.imshow(x_train[2], cmap='gray')
print(y_train[2])
x_train = x_train / 255
x_test = x_test / 255
y_train = utils.to_categorical(y_train)
y_test = utils.to_categorical(y_test)
print(y_train[2])

model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(32, activation='relu'))
model.add(Dense(10, activation='softmax'))
print(model.summary())
model.compile(loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])
history = model.fit(x_train, y_train,
    batch_size=32,
    epochs=10,
    validation_split=0.1)
history.history

import pandas as pd
df = pd.DataFrame(history.history)
print(df)

import seaborn as sns
sns.lineplot(data=df[['loss', 'val_loss']])


