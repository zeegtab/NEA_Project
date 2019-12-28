#Displaying Images with their labels
import os
import numpy as np
import matplotlib as plt
import matplotlib.image as mpimg

train_path = 'train/'

def display(train_path):
    images = os.listdir(train_path+'box/')
    for i in range(0,5):
        j = images[i]
        img = mpimg.imread(train_path+'box/'+j)
        lum_img = img[:, :, 0]
        plt.show(lum_ing)
        imgplot = plt.show(lum_ing)
        plt.colorbar()
        
display(train_path)
