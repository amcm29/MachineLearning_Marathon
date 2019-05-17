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
        if request.form['inputGroupSelect01'] == '1':
            F = 0
            M = 1
        else:
            F = 1
            M = 0

        temperature = int(request.form['inputTemp'])
        input_variables = pd.DataFrame([[bib, age,  inputTime, F, M, temperature]],
                                        columns=['Bib', 'Age', 'Official Time Duration', 'F', 'M','Temp (F)'],
                                        dtype=int)
                                        # index=['input'])

        # model_5K = None

        # def model_5K_f():
            # Load the model from the file
            # global model_5K
            # model_5K = LinearRegression()
        model_5K = joblib.load('model/model_5K.pkl')
        prediction5K = model_5K.predict(input_variables)

        stage_5K = datetime.timedelta(seconds=int(prediction5K[0]))
        print('hi')
        print(stage_5K)
        return render_template('index.html', data=stage_5K)


# model_10K = None

# def load_model_10K():
#     # Load the model from the file
#     global model_10K
#     model_10K = joblib.load('model_10K.pkl')
# prediction10K = model_10K.predict(user_10K_data)

# model_15K = None

# def load_model_15K():
#     # Load the model from the file
#     global model_15K
#     model_15K = joblib.load('model_15K.pkl')
# prediction15K = model_15K.predict(user_15K_data)

# model_20K = None

# def load_model_20K():
#     # Load the model from the file
#     global model_20K
#     model_20K = joblib.load('model_20K.pkl')
# prediction20K = model_20K.predict(user_20K_data)

# model_Half = None

# def load_model_Half():
#     # Load the model from the file
#     global model_Half
#     model_Half = joblib.load('model_Half.pkl')
# predictionHalf = model_Half.predict(user_half_data)

# model_25K = None

# def load_model_25K():
#     # Load the model from the file
#     global model_25K
#     model_25K = joblib.load('model_25K.pkl')
# prediction25K = model_25K.predict(user_25K_data)

# model_30K = None

# def load_model_30K():
#     # Load the model from the file
#     global model_30K
#     model_30K = joblib.load('model_30K.pkl')
# prediction30K = model_30K.predict(user_30K_data)

# model_35K = None

# def load_model_35K():
#     # Load the model from the file
#     global model_35K
#     model_35K = joblib.load('model_35K.pkl')
# prediction35K = model_35K.predict(user_35K_data)

# model_40K = None

# def load_model_40K():
#     # Load the model from the file
#     global model_40K
#     model_40K = joblib.load('model_40K.pkl')
# prediction40K = model_40K.predict(user_40K_data)

# model_Final = None

# def load_model_Final():
#     # Load the model from the file
#     global model_Final
#     model_Final= joblib.load('model_Final.pkl')
# predictionFinal = model_Final.predict(user_final_data)



        # group1 = int(request.form['inputGroupSelect01'])
        
    # if group1 = int('inputGroupSelect01'): 
    #     genderm = '1';
    # elif:
    #     genderm = '0'
            
    #     if group1 = 'Female' then genderf = '1' elif genderf = '0'
            # 'F': int(genderf),
            # 'M': int(genderm),




# df2=pd.DataFrame({'Bib':[25000], 'Age':[42],'Official Time Duration':[22175], 'F':[0], 'M':[1],'Temp (F)':[65]})
# model_5K.predict(df2)



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


if __name__ == '__main__':
    app.run(debug=True) 
