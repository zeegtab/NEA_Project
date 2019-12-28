# Import stuff here
from tkinter import *

import time
import CNN
import os
import cozmoPaparazzi

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
from PIL import Image
import sys

# def module_from_file(module_name, file_path):
# spec = importlib.util.spec_from_file_location(module_name, file_path)
# module = importlib.util.module_from_spec(spec)
# return module


# CNN = module_from_file('CNN', '/Users/zeegtab/Documents/NEA_Project/CNN.py')

# Config the widget
main_col = "#a5d4e6"
title_font = "SF Pro Text Bold"
main_font = "SF Pro Text Medium"
win = Tk()
win.title("Cozmo - Object Recognition")
win.configure(bg=main_col)
to_test = 'empty'

testdir = ['lens-spray', 'medicine']
traindir = ['lens-spray', 'medicine']

# Welcome Header text
wel = Label(win, text="Welcome to Cozmo!", font=(title_font, 50), bg="#a5d4e6")
wel.grid(row=0, column=0)

sep2 = Frame(height=50, bd=0, relief=FLAT, bg="#a5d4e6")
sep2.grid(row=2, column=0, sticky='w')

# Helper Text
header = Label(win,
               text="Add Objects, Train Cozmo or Test Cozmo! For help, click the [?] icon in the top right corner.",
               font=(main_font, 14), bg="#a5d4e6")
header.grid(row=11, column=0, sticky='w')

# New Frame to contain content
separator = Frame(height=5, width=20, bd=0, relief=FLAT, bg="#a5d4e6")
separator.grid(row=12, column=0, sticky='w')

# Add Objects
addobj = Label(separator, text="Add Objects to the Training Directory", font=(main_font, 20), bg="#a5d4e6",
               borderwidth=2,
               relief="groove")
addobj.grid(row=0, column=0, sticky='w')

# Adding Objects Helper Text
train_help = Label(separator, text="Enter the name of the object you would like to add to the list.", bg=main_col)
train_help.grid(row=1, column=0, sticky='w')

# Add Entry Box
ent = Entry(separator, width=50)
ent.grid(row=3, column=0, sticky='w')


# Add to traindir

def add_to_traindir(event, traindir=traindir):
    obj = ent.get()
    if obj == '':
        print("The field is empty! Try typing something in!")
        return
    if not check_testList(obj, traindir):
        response = "Object already exists. Try another object or test Cozmo!"
        print(response)
        return

    dropdown, var = create_dropDown(traindir, "Train on:",7, 0)
    dropdown.grid(sticky='w')

# Button to add objects to traindir
add = Button(separator, text="Add", bg=main_col)
add.grid(row=3, column=1)

# If user clicks on the button to add
add.bind("<Button-1>", add_to_traindir)

# Train Text
train = Label(separator, text="Train Cozmo", font=(main_font, 20), bg="#a5d4e6", borderwidth=2,
              relief="groove")
train.grid(row=5, column=0, sticky='w')


# If user clicks on button to train Cozmo

def trainClick(event):
    val = ent.get()
    ent.delete(0, END)
    ent.config(state='readonly')
    afterText = 'error'
    if val == '':
        print("Field is empty! Cannot train on nothing!")
    elif val == 'Train on:':
        print ("No object selected. Try selecting an object.")
    else:
        print("Will train on " + val + " now.")
        os.system("python3 cozmoPaparazzi.py "+ val)
        afterText = val.upper() + " - TRAINED"
    ent.config(state='normal')
    ent.insert(0, afterText)
    time.sleep(3)

    return


# Train Button
tbutton = Button(separator, text="Train!")
tbutton.grid(row=7, column=1, sticky='w')
tbutton.bind("<Button-1>", trainClick)

# Test Text
test = Label(separator, text="Test Cozmo", font=(main_font, 20), bg="#a5d4e6", borderwidth=2,
             relief="groove")
test.grid(row=8, column=0, sticky='w')

ent.insert(0, "[object name]")
val = ent.get()

# Train Helper text
choose = Label(separator, text="Choose an item from the drop down menu for Cozmo to search for", bg=main_col)
choose.grid(row=6, column=0, sticky='w')

# Test Button
testButton = Button(separator, text="Test Cozmo on selected object")
testButton.grid(row=10, column=0, sticky='w')


def handler(event, testdir=testdir):
    obj = ent.get()
    print(obj)
    ent.delete(0, "end")

    if not check_testList(obj, testdir):
        response = "Object already exists. Try another object or test Cozmo!"
        print(response)
        return
    print(testdir)

    dropdown, var = create_dropDown(testdir, "Select Object",10 , 0)

    def test():
        global to_test
        value = var.get()
        to_test = value
        return

    getTest = Button(separator, text="Get Selected Value", command=test)
    getTest.bind("<Button-1>", next)
    getTest.grid(row=10, column=0)
    return


def create_dropDown(testdir, textvar, rowloc, colloc):
    var = StringVar(win)
    var.set(textvar)
    dropdown = OptionMenu(separator, var, *testdir)
    dropdown.grid(row=rowloc, column=colloc)
    return (dropdown, var)


def check_testList(obj, testdir):
    if obj not in testdir:
        testdir.append(obj)
        return testdir
    else:
        return False


# If object entered, start process
ent.bind("<Return>", handler)


def next(event):
    print(to_test)
    # to_test becomes input to next python script to be run
    CNN.main()


win.mainloop()
