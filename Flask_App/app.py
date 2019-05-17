# import necessary libraries
import numpy as np
import pandas as pd
from flask import Flask, request, redirect, url_for, jsonify, render_template
import pickle
from sklearn.externals import joblib
import datetime
from sklearn.linear_model import LinearRegression

# with open('model_5K.pkl', 'rb') as f:
#     model_5K = pickle.load(f)

model_5K = joblib.load("model/model_5K.pkl")


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # Just render the initial form, to get input
        return(render_template('index.html'))

@app.route("/send", methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        # Extract the input
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
                                        # index=['input'])

        # model_5K = None

        # def model_5K_f():
            # Load the model from the file
            # global model_5K
            # model_5K = LinearRegression()
        model_5K = joblib.load('model/model_5K.pkl')
        prediction5K = model_5K.predict(input_variables5K)

        stage_5K = datetime.timedelta(seconds=int(prediction5K[0]))
        print('hi')
        print(stage_5K)


# model_10K = None

        input_variables10K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K'],
                                        dtype=int)
                                        # index=['input'])


        model_10K = joblib.load('model/model_10K.pkl')
        prediction10K = model_10K.predict(input_variables10K)

        stage_10K = datetime.timedelta(seconds=int(prediction10K[0]))
        print('hi')
        print(stage_10K)
        # return render_template('index.html', data5K = stage_5K, data10K = stage_10K)

# model_15K = None

        input_variables15K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K'],
                                        dtype=int)
                                        # index=['input'])


        model_15K = joblib.load('model/model_15K.pkl')
        prediction15K = model_15K.predict(input_variables15K)

        stage_15K = datetime.timedelta(seconds=int(prediction15K[0]))
        print('hi')
        print(stage_15K)
        # return render_template('index.html', data15K=stage_15K)

# model_20K = None

        input_variables20K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K, prediction15K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K', '15K'],
                                        dtype=int)
                                        # index=['input'])


        model_20K = joblib.load('model/model_20K.pkl')
        prediction20K = model_20K.predict(input_variables20K)

        stage_20K = datetime.timedelta(seconds=int(prediction20K[0]))
        print('hi')
        print(stage_20K)
        # return render_template('index.html', data20K=stage_20K)

# model_Half = None

        input_variablesHalf = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K, prediction15K, prediction20K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K', '15K', '20K'],
                                        dtype=int)
                                        # index=['input'])


        model_Half = joblib.load('model/model_Half.pkl')
        predictionHalf = model_Half.predict(input_variablesHalf)

        stage_Half = datetime.timedelta(seconds=int(predictionHalf[0]))
        print('hi')
        print(stage_Half)
        # return render_template('index.html', dataHalf=stage_Half)

# model_25K = None

        input_variables25K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K, prediction15K, prediction20K, predictionHalf]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K', '15K', '20K', 'Half'],
                                        dtype=int)
                                        # index=['input'])


        model_25K = joblib.load('model/model_25K.pkl')
        prediction25K = model_25K.predict(input_variables25K)

        stage_25K = datetime.timedelta(seconds=int(prediction25K[0]))
        print('hi')
        print(stage_25K)
        # return render_template('index.html', data25K=stage_25K)

# model_30K = None

        input_variables30K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K, prediction15K, prediction20K, predictionHalf, prediction25K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K', '15K', '20K', 'Half', '25K'],
                                        dtype=int)
                                        # index=['input'])


        model_30K = joblib.load('model/model_30K.pkl')
        prediction30K = model_30K.predict(input_variables30K)

        stage_30K = datetime.timedelta(seconds=int(prediction30K[0]))
        print('hi')
        print(stage_30K)
        # return render_template('index.html', data5K = stage_5K, data10K = stage_10K, data15K = stage_15K, data20K = stage_20K, dataHalf = stage_Half, data25K = stage_25K, data30K = stage_30K)

# model_35K = None

        input_variables35K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K, prediction15K, prediction20K, predictionHalf, prediction25K, prediction30K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K', '15K', '20K', 'Half', '25K', '30K'],
                                        dtype=int)
                                        # index=['input'])


        model_35K = joblib.load('model/model_35K.pkl')
        prediction35K = model_35K.predict(input_variables35K)

        stage_35K = datetime.timedelta(seconds=int(prediction35K[0]))
        print('hi')
        print(stage_35K)
        # return render_template('index.html', data5K = stage_5K, data10K = stage_10K, data15K = stage_15K, data20K = stage_20K, dataHalf = stage_Half, data25K = stage_25K, data30K = stage_30K, data35K = stage_35K)

# model_40K = None

        input_variables40K = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K, prediction15K, prediction20K, predictionHalf, prediction25K, prediction30K, prediction35K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K', '15K', '20K', 'Half', '25K', '30K', '35K'],
                                        dtype=int)
                                        # index=['input'])


        model_40K = joblib.load('model/model_40K.pkl')
        prediction40K = model_40K.predict(input_variables40K)

        stage_40K = datetime.timedelta(seconds=int(prediction40K[0]))
        print('hi')
        print(stage_40K)
        # return render_template('index.html', data40K=stage_40K)

# model_Final = None

        input_variablesFinal = pd.DataFrame([[bib, age,  inputTime, F, M, temperature, prediction5K, prediction10K, prediction15K, prediction20K, predictionHalf, prediction25K, prediction30K, prediction35K, prediction40K]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)', '5K', '10K', '15K', '20K', 'Half', '25K', '30K', '35K', '40K'],
                                        dtype=int)
                                        # index=['input'])


        model_Final = joblib.load('model/model_Final.pkl')
        predictionFinal = model_Final.predict(input_variablesFinal)

        stage_Final = datetime.timedelta(seconds=int(predictionFinal[0]))
        print('hi')
        print(stage_Final)
        return render_template('index.html', data5K = stage_5K, data10K = stage_10K, data15K = stage_15K, data20K = stage_20K, dataHalf = stage_Half, data25K = stage_25K, data30K = stage_30K, data35K = stage_35K, data40K = stage_40K, dataFinal = stage_Final)





if __name__ == '__main__':
    app.run(debug=True) 
