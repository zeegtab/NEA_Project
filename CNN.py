#CNN - Convolutional Neural Network
#Purpose: Creates neural network to train on the training data. Then predicts on the testing data.
#Input: training, testing and validation paths, as well as the images to be trained, tested on an validated with.
#Output: CNN and predictions

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
from sklearn.metrics import confusion_matrix
import itertools
import theano
    

def main():

    

    train_path = 'train/'
    valid_path = 'valid/'
    test_path = 'test/'

    train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(224,224),
                                                             classes=['box', 'lens-spray', 'medicine'], batch_size=10)

    valid_batches = ImageDataGenerator().flow_from_directory(valid_path, target_size=(224,224),
                                                             classes=['box', 'lens-spray', 'medicine'], batch_size=4)

    test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(224,224),
                                                            classes=['box', 'lens-spray', 'medicine'], batch_size=10)

    imgs, labels = next(train_batches)

    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)),
        Flatten(),
        Dense(3, activation='softmax'),
    ])

    model.compile(Adam(lr=0.0001), loss = 'categorical_crossentropy', metrics=['accuracy'])
    model.fit_generator(train_batches, steps_per_epoch=4, validation_data=valid_batches, validation_steps=4, epochs=5, verbose=2)

    test_imgs, test_labels = next(test_batches)
    print (test_labels)

    predictions = model.predict_generator(test_batches, steps=1, verbose=0)
    print (predictions)

    '''cm = confusion_matrix(test_labels.argmax(axis=1),predictions.argmax(axis=1))
    np.set_printoptions(precision=2)

    def plot_confusion_matrix(cm, classes, normalize=False, title = 'Confusion matrix', cmap=plt.cm.Blues):
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks= np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print ("normalised")
        else:
            print ("not normalised")

        print (cm)

        thresh = cm.max() / 2
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, cm[i,j],
                     ha="center", va="center",
                     color="white" if cm[i,j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('true label')
        plt.xlabel('prediction label')
        plt.show()

    def plot_confusion_matrix(cm, classes,
                              normalize=False,
                              title='Confusion matrix',
                              cmap=plt.cm.Blues):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')

        print(cm)

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.tight_layout()
        plt.show()


    cm_plot_labels = ['box', 'lens-spray', 'medicine']
    plt.figure()
    plot_confusion_matrix(cm, classes=['box', 'lens-spray', 'medicine'],
                          title='Confusion matrix, without normalization')'''

if __name__ == "__main__":
    main()
