# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 13:19:52 2020

@author: Gokul
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from joblib import load

app = Flask(__name__)
model = pickle.load(open('decison2.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    name=[x for x in request.form.values()]
    name1=name[0]
    name.pop(0)
    x_test = [[float(x) for x in name]]
    print(x_test)
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    if(output==0):
        pred=',there are high probability of you having the chronic kidney disease'
    else:
        pred=",dont worry you have very little risk of having the chronic kidney disease"
    return render_template('main.html', prediction_text='Dear '+name1+'{}'.format(pred))

if __name__ == "__main__":
    app.run(debug=True)
