from flask import Flask, jsonify, redirect, url_for, request, render_template, session
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

import os

###################################################################################################################################################
####DATA BASE######################################################################################################################################
###################################################################################################################################################

# import sqlite3
# import time
# from numpy import genfromtxt
# # from sqlalchemy import Column, Integer, Float, String


# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d


# def Create_DB(db):      
#     #Create DB and format it as needed
#     with sqlite3.connect(db) as conn:
#         conn.row_factory = dict_factory
#         conn.text_factory = str

#         cursor = conn.cursor()

#         cursor.execute("CREATE TABLE [FruitNutrients] ([id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, [name] STRING, [calcium] FLOAT, [carbohydrate] FLOAT, [cholesterol] FLOAT, [cooper] FLOAT, [energy] FLOAT, [saturated] FLOAT, [fiber_total] FLOAT, [glucose] FLOAT, [iron] FLOAT, [magnesium] FLOAT, [phosphorum] FLOAT, [potassium] FLOAT, [protein] FLOAT, [sodium] FLOAT, [starch] FLOAT, [sucrose] FLOAT, [total_fat] FLOAT, [vitamin_c] FLOAT, [vitamin_d] FLOAT, [vitamin_e] FLOAT, [water] FLOAT, [zinc] FLOAT);")


# def Add_Record(db, data):
#     #Insert record into table
#     with sqlite3.connect(db) as conn:
#         conn.row_factory = dict_factory
#         conn.text_factory = str
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO fruits({cols}) VALUES({vals});".format(cols = str(data.keys()), vals=str([data[i] for i in data])  ))
                    


# def Load_Data(file_name):
#     data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
#     return data.tolist()


# db = 'fruits.db' #Database filename 
# file_name = "fruits.csv" #sample CSV file used:  http://www.google.com/finance/historical?q=NYSE%3AT&ei=W4ikVam8LYWjmAGjhoHACw&output=csv

# data = Load_Data(file_name) #Get data from CSV

# Create_DB(db) #Create DB

# #For every record, format and insert to table
# for i in data:
#     record = {
#             'name' : i[0],
#             'calcium' : i[1],
#             'carbohydrate' : i[2],
#             'copper' : i[3],
#             'energy' : i[4],
#             'saturated_fat' : i[5],
#             'fiber_total' : i[6],
#             'glucose' : i[7],
#             'iron' : i[8],
#             'magnesium' : i[9],
#             'phosporum' : i[10],
#             'potassium' : i[11],
#             'protein' : i[12],
#             'sodium' : i[13],
#             'starch' : i[14],
#             'sucrose' : i[15],
#             'total_fat' : i[16],
#             'vitamin_c' : i[17],
#             'vitamin_d' : i[18],
#             'vitamin_e' : i[19],
#             'water' : i[20],
#             'zinc' : i[21]
#         }
#     Add_Record(db, record)
##################################

# #########################################################
# from numpy import genfromtxt
# from sqlalchemy import Column, Integer, Float, Date, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, Session
# from flask_sqlalchemy import SQLAlchemy

# def Load_Data(file_name):
#     data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
#     return data.tolist()

# Base = declarative_base()

# class Fruits(Base):
#     #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
#     __tablename__ = 'fruits'
#     __table_args__ = {'sqlite_autoincrement': True}
#     #tell SQLAlchemy the name of column and its attributes:
#     id = Column(Integer, primary_key=True, nullable=False) 
#     name = Column(String)
#     calcium = Column(Float)
#     carbohydrate = Column(Float)
#     copper = Column(Float)
#     energy = Column(Float)
#     saturated_fat = Column(Float)
#     fiber_total = Column(Float)
#     glucose = Column(Float)
#     iron = Column(Float)
#     magnesium = Column(Float)
#     phosphorum = Column(Float)
#     potassium = Column(Float)
#     protein = Column(Float)
#     sodium = Column(Float)
#     starch = Column(Float)
#     sucrose = Column(Float)
#     total_fat = Column(Float)
#     vitamin_c = Column(Float)
#     vitamin_d = Column(Float)
#     vitamin_e = Column(Float)
#     water = Column(Float)
#     zinc = Column(Float)
    
# #Create the database
# engine = create_engine('sqlite:///fruits.db')
# Base.metadata.create_all(engine)

# #Create the session
# sess = sessionmaker()
# sess.configure(bind=engine)
# s = Session()

# file_name = "fruits.csv" 
# data = Load_Data(file_name) 


# for i in data:
#     record = Fruits(**{
#         'name' : i[0],
#         'calcium' : i[1],
#         'carbohydrate' : i[2],
#         'copper' : i[3],
#         'energy' : i[4],
#         'saturated_fat' : i[5],
#         'fiber_total' : i[6],
#         'glucose' : i[7],
#         'iron' : i[8],
#         'magnesium' : i[9],
#         'phosphorum' : i[10],
#         'potassium' : i[11],
#         'protein' : i[12],
#         'sodium' : i[13],
#         'starch' : i[14],
#         'sucrose' : i[15],
#         'total_fat' : i[16],
#         'vitamin_c' : i[17],
#         'vitamin_d' : i[18],
#         'vitamin_e' : i[19],
#         'water' : i[20],
#         'zinc' : i[21]
#     })
# s.add(record) #Add all the records

# s.commit() #Attempt to commit all the records

# # s.close() #Close the connection

# # sessionQuery = Session()
# # queryOne = sessionQuery.query(fruits.name).first()
# # print(queryOne)
    
# ####&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*******************************************
# import sqlite3
# import csv

# conn = sqlite3.connect('fruits.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS fruit_nutrients')
# cur.execute('''
# CREATE TABLE "fruit_nutrients"(
#     "name" TEXT,
#     "calcium" REAL,
#     "carbohydrate" REAL,
#     "copper" REAL,
#     "energy" REAL,
#     "saturated_fat" REAL,
#     "fiber_total" REAL,
#     "glucose" REAL,
#     "iron" REAL,
#     "magnesium" REAL,
#     "phosphorum" REAL,
#     "potassium" REAL,
#     "protein" REAL,
#     "sodium" REAL,
#     "starch" REAL,
#     "sucrose" REAL,
#     "total_fat" REAL,
#     "vitamin_c" REAL,
#     "vitamin_d" REAL,
#     "vitamin_e" REAL,
#     "water" REAL,
#     "zinc" REAL
# )
# ''')

# with open("fruits2.csv", 'r') as csv_file:
#     for row in csv_file:
#         print(len(row.split(",")))
#         cur.execute("INSERT INTO fruit_nutrients VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.split(","))
#         conn.commit()
# conn.close()


###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*********************************************

    # csv_reader = csv.reader(csv_file, delimiter=',')
    # for i in csv_reader:
    #     print(i),
    #     name = i[0],
    #     calcium = float(i[1]),
    #     carbohydrate = float(i[2]),
    #     copper =  float(i[3]),
    #     energy = float(i[4]),
    #     saturated_fat = float(i[5]),
    #     fiber_total = float(i[6]),
    #     glucose = float(i[7]),
    #     iron = float(i[8]),
    #     magnesium = float(i[9]),
    #     phosphorum = float(i[10]),
    #     potassium = float(i[11]),
    #     protein = float(i[12]),
    #     sodium = float(i[13]),
    #     starch = float(i[14]),
    #     sucrose = float(i[15]),
    #     total_fat = float(i[16]),
    #     vitamin_c = float(i[17]),
    #     vitamin_d = float(i[18]),
    #     vitamin_e = float(i[19]),
    #     water = float(i[20]),
    #     zinc = float(i[21])
        #  cur.execute('''INSERT INTO fruit_nutrients(name,calcium,carbohydrate,copper,energy,saturated_fat,fiber_total,glucose,iron,magnesium,phosphorum,potassium,protein,sodium,starch,sucrose,total_fat,vitamin_c,vitamin_d,vitamin_e,water,zinc)
        # VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(name,calcium,carbohydrate,copper,energy,saturated_fat,fiber_total,glucose,iron,magnesium,phosphorum,potassium,protein,sodium,starch,sucrose,total_fat,vitamin_c,vitamin_d,vitamin_e,water,zinc))
        # conn.commit()


###################################################################################################################################################
###MODEL PREDICTION################################################################################################################################
###################################################################################################################################################

import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy
import tensorflow as tf
from tensorflow import keras

#load the trained model to classify the images
from keras.models import load_model

model = load_model('fruits_tensorflow-100-New10-360.h5')

#dictionary to label all the dataset classes.
classes = { 
    0:'apple',
    1:'banana',
    2:'blueberry',
    3:'fig',
    4:'lemon',
    5:'orange',
    6:'peach',
    7:'persimmon',
    8:'tomato',
    9:'watermelon'
}

def classify(file_path):
    img = keras.preprocessing.image.load_img(
        file_path, target_size=(180, 180))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict_classes(img_array)[0]
    sign = classes[predictions]
    return sign



###################################################################################################################################################
###FLASK APP#######################################################################################################################################
###################################################################################################################################################



app = Flask(__name__)
dropzone = Dropzone(app)

app.config['SECRET_KEY'] = 'supersecretkey'


# Dropzone settings
# app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'
# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB



@app.route("/", methods = ["GET", "POST"])
def index():
    # set session for image results
    if "file_urls" not in session:
        session['file_urls'] = []

    if "prediction" not in session:
        session['prediction'] = []


    # list to hold our uploaded image urls
    file_urls = session['file_urls']
    prediction = session['prediction']

    # handle image upload from Dropzone
    if request.method == "POST":
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)
            print("file type")
            print(type(file))

            # save the file with to our photos folder
            filename = photos.save(file, name=file.filename)
            # print("RESULT NEW*********************************************")
            path_image = f'./uploads/{filename}'
            # print(path_image)
            # print("RESULT NEW*********************************************")
            resultPrediction = classify(path_image)
            # print("RESULT NEW*********************************************")
            # print(resultPrediction)
            # print("RESULT NEW*********************************************")


            # append image urls
            file_urls.append(photos.url(filename))
            prediction.append(resultPrediction)
            # print(file.filename)
        
        session['file_urls'] = file_urls
        session['prediction'] = prediction
        return "uploading..."

    # return dropzone template on GET request  
    return render_template('index.html')

@app.route('/results')
def results():
    # redirect to home if no images to display
    if "file_urls" not in session or session['file_urls'] == []:
        return redirect(url_for('index'))
        
    # set the file_urls and remove the session variable
    file_urls = session['file_urls']
    session.pop('file_urls', None)
    prediction = session['prediction']
    session.pop('prediction', None)

    return render_template('results.html', file_urls=file_urls, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)