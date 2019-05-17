# PLAIDML COMPATABILITY CODE
import plaidml.keras
plaidml.keras.install_backend()
####################################

import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
# from keras.layers import Model, Input
# from keras.layers.merge import concatenate

import os
import pandas as pd
import numpy as np
from keras_preprocessing import image

# import all normalized images
directory = "DEEPstruc_Normalized"
imageSet = [image.load_img(directory + "/" + path) for path in os.listdir(directory)]
X_img = [image.img_to_array(img) for img in imageSet]
X_img = np.array(X_img)
print("Number of images: ", len(imageSet))
print("Image resolution: ", imageSet[0].size)
print(imageSet[0].getbands())
print(X_img.shape)

# data import
label_data = pd.read_csv("label_property_one_hot_encoded.csv", header=0)
label_data.head()
mag_data = label_data[["mag__AFM", "mag__FM", "mag__NM"]] # y data
mag_data.head()
print(mag_data.shape)

# simple model definition to predict magnetism classification
model = Sequential()
model.add(
    Conv2D(
        5, 
        kernel_size=3, 
        activation='relu', 
        input_shape=X_img.shape[1:4]
    )
)

model.add(Flatten())
model.add(Dense(3, activation='softmax')) # three categories of Magnetism

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(X_img, mag_data, validation_split=0.2, epochs=10, callbacks=[keras.callbacks.EarlyStopping()])





