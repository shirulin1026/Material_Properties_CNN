
#using GPU

import numpy as np
import keras
np.random.seed(1337)
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation, Convolution2D, MaxPooling2D, Flatten
from keras.optimizers import Adam

import os
import pandas as pd
from keras.preprocessing import image

'''
#using colab to upload data, upload zip documents for pic folder, and upload csv
from google.colab import files
files.upload()
from google.colab import files
files.upload()

# x data import
!unzip NEWDEEP.rar
'''


directory = "NEWDEEP"
imageSet = [image.load_img(directory + "/" + path) for path in os.listdir(directory)]
X = [image.img_to_array(img) for img in imageSet]
X = np.array(X)
print("Number of images: ", len(imageSet))
print("Image resolution: ", imageSet[0].size)
print(imageSet[0].getbands())
print(X.shape)

# y data import
label_data = pd.read_csv("label_property_one_hot_encoded.csv", header=0)
label_data.head()
mag_data = label_data[["mag__AFM", "mag__FM", "mag__NM"]] # y data
y = mag_data
y.head()
print(y.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

model=Sequential()

model.add(Convolution2D(
    filters=32,
    kernel_size=5,
    border_mode='same',
    input_shape=(500,500,3),
))
model.add(Activation('relu'))
model.add(MaxPooling2D(
    pool_size=(5,5),
    strides=(2,2),
    border_mode='same'
))

model.add(Convolution2D(64,5, border_mode='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(5,5),border_mode='same')) #20, 20, 64
model.add(MaxPooling2D(pool_size=(2,2),border_mode='same')) #10,10,64

model.add(Flatten())
model.add(Dense(3200))
model.add(Activation('relu'))

model.add(Dense(990))
model.add(Activation('relu'))

model.add(Dense(3))
model.add(Activation('softmax'))

adam=Adam(lr=1e-4)

model.compile(optimizer=adam,
                loss='categorical_crossentropy',
                metrics=['accuracy'])


print('Training-------')

model.fit(X_train,y_train,
    epochs=10,
    batch_size=32,
    callbacks=[keras.callbacks.EarlyStopping()])

print('\nTesting------')
loss,accuracy=model.evaluate(X_test,y_test)

print('\ntest loss:', loss)
print('\ntest accuracy', accuracy)

# save model description
model_json = model.to_json()
with open("model_sr1.json", "w") as json_file:
    json_file.write(model_json)

# save model trained-weights
model.save_weights("model_sr1_weights.h5")
