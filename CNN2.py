#CNN2 - Electric Boogaloo
#Trying this out again because its taking too long otherwise

import os
import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import *
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import itertools
import matplotlib.pyplot as plt

train_path = 'train/'
valid_path = 'valid/'
test_path = 'test/'

train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(224,224), classes=['box', 'lens-spray', 'medicine'], batch_size=10)
print (train_batches)
valid_batches = ImageDataGenerator().flow_from_directory(valid_path, target_size=(224,224), classes=['box', 'lens-spray', 'medicine'], batch_size=4)
print (valid_batches)
test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(224,224), classes=['box', 'lens-spray', 'medicine'], batch_size=10)

imgs, labels = next(train_batches)

print (labels)

model = Sequential([
    Conv2D(32, (3, 3), activation = 'relu', input_shape = (224,224,3)),
    Flatten(),
    Dense(3, activation = 'softmax'),
    ])

model.compile(Adam(lr=0.0001), loss = 'categorical_crossentropy', metrics=['accuracy'])

model.fit_generator(train_batches, steps_per_epoch = 4, validation_data = valid_batches, validation_steps = 4, epochs = 5, verbose = 2)

