import time
import sys
import os
import random
import shutil

#Purpose: Splits photos taken by Cozmo into training, testing, and validation subfolders to prepare for CNN

#iMAC: /Users/ZTab/Documents/2018-2020 St. Olaves/Computer Science (A Level)/NEA_Project
#MacBook Pro: /Users/zeegtab/Documents/NEA_Project

PROJECT_HOME = '/Users/zeegtab/Documents/NEA_Project'

if PROJECT_HOME == "":
    print ("PROJECT_HOME empty, quitting")
    sys.exit()

shutil.rmtree('data')
shutil.rmtree('test')
shutil.rmtree('train')
shutil.rmtree('valid')

print ('copying raw_data into data')
shutil.copytree('raw_data', 'data')

sdir = os.listdir('data')
sdir.remove('.DS_Store')
print (sdir)
tdir = ['test', 'train', 'valid']

#Create source directories if they don't exist
for i in tdir:
    if not os.path.exists(i):
        os.makedirs(i)
        print ("made directory " + i)
    for j in sdir:
        tpath = i + '/' + j
        if not os.path.exists(tpath):
            os.makedirs(tpath)
            print ("made directory " + tpath)
    

#Organizes images into test, train and valid folders
def train(sdir):
    train_size = 0.8
    for i in sdir:
        cdir = 'data/'+i
        photos = os.listdir(cdir)
        print (len(photos)+1)
        train_num = int((len(photos))*train_size)
        to_train = random.sample(photos, k=train_num)
        for k in range(0,len(to_train)-1):
            sfile = to_train[k]
            # print ('COPYING: ' + PROJECT_HOME + '/' + cdir + '/' + sfile + 'TO: ' + PROJECT_HOME +
            #'/train/' + i + '_train/' + sfile)
            shutil.move(PROJECT_HOME + '/' + cdir + '/' + sfile, PROJECT_HOME + '/train/' +
                        i + '/' + sfile)
        

train(sdir)

def test(sdir):
    for i in sdir:
        cdir = 'data/'+i
        rem = os.listdir(cdir)
        for k in rem:
            shutil.move(PROJECT_HOME + '/' + cdir + '/' + k, PROJECT_HOME + '/test/' + i + '/' + k)

test(sdir)

def valid(sdir):
    vsize = 0.2
    for i in sdir:
        cdir = 'train/' + i
        photos = os.listdir(cdir)
        valid_num = int((len(photos)*vsize))
        to_valid = random.sample(photos, k=valid_num)
        for k in range(0, len(to_valid)-1):
            sfile = to_valid[k]
            shutil.move(PROJECT_HOME + '/' + cdir + '/' + sfile, PROJECT_HOME + '/valid/' +
                        i + '/' + sfile)

valid(sdir)
