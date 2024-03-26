import tensorflow as tf
from tensorflow.keras import utils
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense, Input
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model

data = tf.keras.datasets.fashion_mnist.load_data()
(x_train, y_train), (x_test, y_test) = data
print(y_train, len(y_train), set(y_train))
y_train = utils.to_categorical(y_train)
y_test = utils.to_categorical(y_test)

model = Sequential([
    Input(shape=(28, 28)),  # 入力層として Input を使用
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

print(model.summary())
model.compile(loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])
model.fit(x_train, y_train, batch_size    =32, epochs=5)
model.save('my_model.h5')  # HDF5ファイルとして保存

model.evaluate(x_test, y_test)

#モデルを再読み込み
loaded_model = load_model('my_model.h5')
print(loaded_model.evaluate(x_test, y_test))
