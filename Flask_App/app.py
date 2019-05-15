# import necessary libraries
import os
import io
import numpy as numpy

from flask import Flask, request, redirect, url_for, jsonify, render_template

import pickle
from sklearn.externals import joblib

import datetime

app = Flask(__name__)

model_5K = None

def load_model_5K():
    # Load the model from the file
    global model_5K
    model_5K = joblib.load('model_5K.pk1')
load_model_5K()

model_10K = None

def load_model_10K():
    # Load the model from the file
    global model_10K
    model_10K = joblib.load('model_10K.pk1')
load_model_10K()

model_15K = None

def load_model_15K():
    # Load the model from the file
    global model_15K
    model_15K = joblib.load('model_15K.pk1')
load_model_15K()

model_20K = None

def load_model_20K():
    # Load the model from the file
    global model_20K
    model_20K = joblib.load('model_20K.pk1')
load_model_20K()

model_Half = None

def load_model_Half():
    # Load the model from the file
    global model_Half
    model_Half = joblib.load('model_Half.pk1')
load_model_Half()

model_25K = None

def load_model_25K():
    # Load the model from the file
    global model_25K
    model_25K = joblib.load('model_25K.pk1')
load_model_25K()

model_30K = None

def load_model_30K():
    # Load the model from the file
    global model_30K
    model_30K = joblib.load('model_30K.pk1')
load_model_30K()

model_35K = None

def load_model_35K():
    # Load the model from the file
    global model_35K
    model_35K = joblib.load('model_35K.pk1')
load_model_35K()

model_40K = None

def load_model_40K():
    # Load the model from the file
    global model_40K
    model_40K = joblib.load('model_40K.pk1')
load_model_40K()

model_Final = None

def load_model_Final():
    # Load the model from the file
    global model_Final
    model_Final= joblib.load('model_Final.pk1')
load_model_Final()



@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        bib_number = int(request.form['inputBib'])
        age = int(request.form['inputAge'])
        # group1 = int(request.form['inputGroupSelect01'])
        
    # if group1 = int('inputGroupSelect01'): 
    #     genderm = '1';
    # elif:
    #     genderm = '0'
            
    #     if group1 = 'Female' then genderf = '1' elif genderf = '0'
        temperature = float(request.form['inputTemp'])
        timeh = int(request.form['inputHours'])
        timem = int(request.form['inputMinutes'])
        form_data = {
            'Bib': int(bib_number),
            'Age': int(age),
            'receivedHours': int(timeh),
            'receivedMinutes': int(timem),
            # 'F': int(genderf),
            # 'M': int(genderm),
            'Temp (F)': int(temperature)
        }

seconds_in_hour = 3600
seconds_in_minute = 60

seconds = int(input('Enter a number of seconds: '))

hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)

minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)

# concat('{1:.0f} hours, {2:.0f} minutes, {3:.0f} seconds.'.format(hours, minutes, seconds))

# df2=pd.DataFrame({'Bib':[25000], 'Age':[42],'Official Time Duration':[22175], 'F':[0], 'M':[1],'Temp (F)':[65]})
# model_5K.predict(df2)

# datatime = str(datetime.timedelta(seconds = (data5)))



dataList = []


# # Use the loaded model to make predictions
# data5 = model_5K_from_joblib.predict()
# data10 = model_10K_from_joblib.predict()
# data15 = model_15K_from_joblib.predict()
# data20 = model_20K_from_joblib.predict()
# dataHalf = model_Half_from_joblib.predict()
# data25 = model_25K_from_joblib.predict()
# data30 = model_30K_from_joblib.predict()
# data35 = model_35K_from_joblib.predict()
# data40 = model_40K_from_joblib.predict()
# dataFinal = model_Final_from_joblib.predict()



# dataList.append.data5
# dataList.append.data10
# dataList.append.data15
# dataList.append.data20
# dataList.append.dataHalf
# dataList.append.data25
# dataList.append.data30
# dataList.append.data35
# dataList.append.data40
# dataList.append.Final

        
# if request.method == 'GET':
#    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True) 
