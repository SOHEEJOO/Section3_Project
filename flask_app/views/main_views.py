from flask import Blueprint, render_template, request
import pickle
import numpy as np
import joblib
#from flask_app.models import User

bp = Blueprint('main', __name__, url_prefix='/')

with open('flask_app/model.pkl', 'rb') as f:
    model = joblib.load(f)

@bp.route('/')
def hello():
    return render_template('home.html')

@bp.route('/predict', methods=['GET','POST'])
def home():
    data1 =request.form['budget']
    data2 =request.form['runtime']
    arr = np.array([[data1, data2]])
    pred = model.predict(arr)
    return render_template('predict.html', data=pred)

