# https://data-flair.training/blogs/image-classification-deep-learning-project-python-keras/

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

#load the trained model to classify the images
from keras.models import load_model

model = load_model('fruits_tensorflow.h5')

#dictionary to label all the dataset classes.
classes = { 
    0:'apple',
    1:'banana',
    2:'blueberry',
    3:'lemon',
    4:'mango',
    5:'orange',
    6:'peach',
    7:'persimmon',
    8:'strawberry',
    9:'tomato',
    10:'watermelon'
}

#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Image Classification Fruits')
top.configure(background='#CDCDCD')
label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed

    img = keras.preprocessing.image.load_img(
        file_path, target_size=(180, 180))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    # predict = model.predict(img_array)
    predictions = model.predict_classes(img_array)[0]
    # score = tf.nn.softmax(predict[0])
    # score = model.predict_proba(img_array)[0]
    # score = model.evaluate(img_array)
    score = model.predict(img_array)

    
    sign = classes[predictions]
    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(classes[numpy.argmax(score)], 100 * numpy.max(score))
    )
    # print(f'{sign}')
    label.configure(foreground='#011638', text=sign) 

def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",
        command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',
        font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),
            (top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image, padx=10,pady=5)

upload.configure(background='#364156', foreground='white', font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Image Classification Fruit",pady=20, font=('arial',20,'bold'))

heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()