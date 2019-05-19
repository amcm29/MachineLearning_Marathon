# import necessary libraries
import numpy as np
import pandas as pd
from flask import Flask, request, redirect, url_for, jsonify, render_template
import pickle
from sklearn.externals import joblib
import datetime
from sklearn.linear_model import LinearRegression


# Load the model for the appropriate stage of the marathon.
model_5K = joblib.load("model/model_5K.pkl")


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # Just render the initial form, to get input
        return(render_template('index.html'))

@app.route("/machine.html", methods=['GET', 'POST'])
def machine():
    if request.method == 'POST':
        return redirect(url_for("index"))
    return render_template('machine.html')

@app.route("/send", methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        # Extract the input supplied by the user from the HTML page.
        bib = int(request.form['inputBib'])
        age = int(request.form['inputAge'])
        timeh = int(request.form['inputHours'])
        timeHsec=timeh*3600
        timem = int(request.form['inputMinutes'])
        timeMsec=timem*60
        inputTime = (timeMsec + timeHsec)
        if request.form['inputGroupSelect01'] == "1":
            F = 0
            M = 1
        else:
            F = 1
            M = 0
        print(request.form['inputGroupSelect01'])
        temperature = int(request.form['inputTemp'])
        input_variables5K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)'],
                                        dtype=int)


# model_5K = None
# Load the model for the appropriate stage of the marathon.
        model_5K = joblib.load('model/model_5K.pkl')
# Capture the seconds predicted by the model.
        prediction5K = model_5K.predict(input_variables5K)
# Convert the seconds to minutes and hours and seconds.
        stage_5K = datetime.timedelta(seconds=int(prediction5K[0]))

# model_10K = None
# Bring in all the inputs for the model making sure to include the predictions from previous models.
        input_variables10K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K'],
                                        dtype=int)
# Load the model for the appropriate stage of the marathon.
        model_10K = joblib.load('model/model_10K.pkl')
# Capture the seconds predicted by the model.
        prediction10K = model_10K.predict(input_variables10K)
# Convert the seconds to minutes and hours and seconds.
        stage_10K = datetime.timedelta(seconds=int(prediction10K[0]))

# model_15K = None
# Bring in all the inputs for the model making sure to include the predictions from previous models.
        input_variables15K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K'],
                                        dtype=int)
# Load the model for the appropriate stage of the marathon.
        model_15K = joblib.load('model/model_15K.pkl')
        prediction15K = model_15K.predict(input_variables15K)
# Convert the seconds to minutes and hours and seconds.
        stage_15K = datetime.timedelta(seconds=int(prediction15K[0]))

# model_20K = None
# Bring in all the inputs for the model making sure to include the predictions from previous models.
        input_variables20K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K, prediction15K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K', '15K'],
                                        dtype=int)
# Load the model for the appropriate stage of the marathon.
        model_20K = joblib.load('model/model_20K.pkl')
        prediction20K = model_20K.predict(input_variables20K)
# Convert the seconds to minutes and hours and seconds.
        stage_20K = datetime.timedelta(seconds=int(prediction20K[0]))

# model_Half = None
# Bring in all the inputs for the model making sure to include the predictions from previous models.
        input_variablesHalf = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K, prediction15K, prediction20K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K', '15K', '20K'],
                                        dtype=int)
# Load the model for the appropriate stage of the marathon.
        model_Half = joblib.load('model/model_Half.pkl')
        predictionHalf = model_Half.predict(input_variablesHalf)
# Convert the seconds to minutes and hours and seconds.
        stage_Half = datetime.timedelta(seconds=int(predictionHalf[0]))

# model_25K = None
# Bring in all the inputs for the model making sure to include the predictions from previous models.
        input_variables25K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K, prediction15K, prediction20K, predictionHalf]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K', '15K', '20K', 'Half'],
                                        dtype=int)
# Load the model for the appropriate stage of the marathon.
        model_25K = joblib.load('model/model_25K.pkl')
        prediction25K = model_25K.predict(input_variables25K)
# Convert the seconds to minutes and hours and seconds.
        stage_25K = datetime.timedelta(seconds=int(prediction25K[0]))

# model_30K = None
# Bring in all the inputs for the model making sure to include the predictions from previous models.
        input_variables30K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K, prediction15K, prediction20K, predictionHalf, prediction25K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K', '15K', '20K', 'Half', '25K'],
                                        dtype=int)
# Load the model for the appropriate stage of the marathon.
        model_30K = joblib.load('model/model_30K.pkl')
        prediction30K = model_30K.predict(input_variables30K)
# Convert the seconds to minutes and hours and seconds.
        stage_30K = datetime.timedelta(seconds=int(prediction30K[0]))

# model_35K = None
# Bring in all the inputs for the model making sure to include the predictions from previous models.
        input_variables35K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K, prediction15K, prediction20K, predictionHalf, prediction25K, prediction30K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K', '15K', '20K', 'Half', '25K', '30K'],
                                        dtype=int)
# Load the model for the appropriate stage of the marathon.
        model_35K = joblib.load('model/model_35K.pkl')
        prediction35K = model_35K.predict(input_variables35K)
# Convert the seconds to minutes and hours and seconds.
        stage_35K = datetime.timedelta(seconds=int(prediction35K[0]))

# model_40K = None
# Bring in all the inputs for the model making sure to include the predictions from previous models.
        input_variables40K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K, prediction15K, prediction20K, predictionHalf, prediction25K, prediction30K, prediction35K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K', '15K', '20K', 'Half', '25K', '30K', '35K'],
                                        dtype=int)
# Load the model for the appropriate stage of the marathon.
        model_40K = joblib.load('model/model_40K.pkl')
        prediction40K = model_40K.predict(input_variables40K)
# Convert the seconds to minutes and hours and seconds.
        stage_40K = datetime.timedelta(seconds=int(prediction40K[0]))
# Render the results of the calculations from the models to the HTML page.
        # return render_template('index.html', data5K = stage_5K, data10K = stage_10K, data15K = stage_15K, data20K = stage_20K, dataHalf = stage_Half, data25K = stage_25K, data30K = stage_30K, data35K = stage_35K, data40K = stage_40K)


# model_Final = None
# Bring in all the inputs for the model making sure to include the predictions from previous models.
        input_variablesFinal = pd.DataFrame([[bib, age, F, M, temperature, prediction5K, prediction10K, prediction15K, prediction20K, predictionHalf, prediction25K, prediction30K, prediction35K, prediction40K]],
                                        columns=['Bib', 'Age', 'F', 'M','Temp (F)', '5K', '10K', '15K', '20K', 'Half', '25K', '30K', '35K', '40K'],
                                        dtype=int)
# Load the model for the appropriate stage of the marathon.
        model_Final = joblib.load('model/model_Final.pkl')
        predictionFinal = model_Final.predict(input_variablesFinal)
# Convert the seconds to minutes and hours and seconds.
        stage_Final = datetime.timedelta(seconds=int(predictionFinal[0]))
# Render the results of the calculations from the models to the HTML page.
        return render_template('index.html', data5K = stage_5K, data10K = stage_10K, data15K = stage_15K, data20K = stage_20K, dataHalf = stage_Half, data25K = stage_25K, data30K = stage_30K, data35K = stage_35K, data40K = stage_40K, dataFinal = stage_Final)

if __name__ == '__main__':
    app.run(debug=True) 