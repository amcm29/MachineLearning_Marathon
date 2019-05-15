# import necessary libraries
from flask import (
    Flask,
    render_template,
    request)

import pickle
from sklearn.externals import joblib

import datetime

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "GET":
        bib_number = int(request.form["inputBib"])
        age = int(request.form["inputAge"])
        group1 = int(request.form["inputGroupSelect01"])
        if group1 = "Male" then genderm = "1" else genderm = "0"
        if group1 = "Female" then genderf = "1" else genderf = "0"
        temperature = float(request.form["inputTemp"])
        timeh = int(request.form["inputHours"])
        timem = int(request.form["inputMinutes"])
        form_data = {
            "Bib": int(bib_number),
            "Age": int(age),
            "Official Time Duration": int(time),
            "F": int(genderf),
            "M": int(genderm),
            "Temp (F)": int(temperature)
        }


seconds_in_hour = 3600
seconds_in_minute = 60

seconds = int(input("Enter a number of seconds: "))

hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)

minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)

concat("{1:.0f} hours, {2:.0f} minutes, {3:.0f} seconds.".format(hours, minutes, seconds))

df2=pd.DataFrame({'Bib':[25000], 'Age':[42],'Official Time Duration':[22175], 'F':[0], 'M':[1],'Temp (F)':[65]})
model_5K.predict(df2)

datatime = str(datetime.timedelta(seconds = (data5)))



dataList = []

# Load the model from the file
model_5K_from_joblib = joblib.load('model_5K.pkl')
model_10K_from_joblib = joblib.load('model_10K.pkl')
model_15K_from_joblib = joblib.load('model_15K.pkl')
model_20K_from_joblib = joblib.load('model_20K.pkl')
model_Half_from_joblib = joblib.load('model_Half.pkl')
model_25K_from_joblib = joblib.load('model_25K.pkl')
model_30K_from_joblib = joblib.load('model_30K.pkl')
model_35K_from_joblib = joblib.load('model_35K.pkl')
model_40K_from_joblib = joblib.load('model_40K.pkl')
model_Final_from_joblib = joblib.load('model_Final.pkl')


# Use the loaded model to make predictions
data5 = model_5K_from_joblib.predict(form_data)
data10 = model_10K_from_joblib.predict(form_data)
data15 = model_15K_from_joblib.predict(form_data)
data20 = model_20K_from_joblib.predict(form_data)
dataHalf = model_Half_from_joblib.predict(form_data)
data25 = model_25K_from_joblib.predict(form_data)
data30 = model_30K_from_joblib.predict(form_data)
data35 = model_35K_from_joblib.predict(form_data)
data40 = model_40K_from_joblib.predict(form_data)
dataFinal = model_Final_from_joblib.predict(form_data)



dataList.append.data5
dataList.append.data10
dataList.append.data15
dataList.append.data20
dataList.append.dataHalf
dataList.append.data25
dataList.append.data30
dataList.append.data35
dataList.append.data40
dataList.append.Final





return render_template('index.html', bib = bib, age = age, group1="1", group2="2", temperature = temperature, datatime)
        
if request.method == "GET":
   return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True) 
