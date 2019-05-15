# import necessary libraries
from flask import (
    Flask,
    render_template,
    request)

import pickle
from sklearn.externals import joblib

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        bib_number = int(request.form["bib"])
        age = int(request.form["age"])
        group1 = int(request.form["1"])
        group2 = int(request.form["2"])
        temperature = float(request.form["temp"])
        hours = int(request.form["timeHours"])
        minutes = float(request.form["timeMinutes"])
        form_data = {
            "bib": int(bib_number),
            "age": int(age),
            "1": group1,
            "2": group2,
            "temp": temperature,
            "timeHours": hours,
            "timeMinutes": minutes
        }

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


        return render_template('index.html', bib = bib, age = age, group1="1", group2="2", temperature = temperature, hours = hours, minutes = minutes)
        
    if request.method == "GET":
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True) 
