import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from sklearn.model_selection import train_test_split
from keras.utils import plot_model


seed = 9
np.random.seed(seed)

X = pd.read_csv('input.csv')
Y = pd.read_csv('output.csv')

(X_train, X_test, Y_train, Y_test) = train_test_split(X, Y, test_size=0.33, random_state=seed)

model = Sequential()
model.add(Dense(512, activation="relu", kernel_initializer="uniform", input_dim=5))
model.add(Dense(6, activation="relu", kernel_initializer="uniform"))
model.add(Dense(10, activation=tf.nn.softmax))
model.add(Dense(5, activation="sigmoid", kernel_initializer="uniform"))

from keras.optimizers import SGD
opt = SGD(lr=0.00001)
model.compile(loss = "binary_crossentropy", optimizer = opt, metrics=['accuracy'])

model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=100, batch_size=1)

scores = model.evaluate(X_test, Y_test)
print ("Accuracy: %.2f%%" %(scores[1]*100))
print ("Loss: %.2f%%" %(scores[0]))

plot_model(model, to_file='model.png')
