import numpy

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

numpy.random.seed(42)

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 748)
#X_test = X_test.reshape(10000, 748)

X_train = X_train.astype("float32")
#X_test = X_test.astype("float32")
X_train /= X_train
#X_test /= X_test

y_train = np_utils.to_categorical(y_train, 10)
#y_test = np_utils.to_categorical(y_test, 10)

model = Sequential()

model.add(Dense(800, input_dim=784, init="normal", activation="relu"))
model.add(Dense(10, init="normal", activation="softmax"))

model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])

print(model.summary())

#model.fit(X_train, y_train, batch_size=200, nb_epoch=100, verbose=1)

