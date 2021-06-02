from flask import Blueprint, render_template, request, jsonify
import pickle
import numpy as np
import joblib
from flask_app.models import User, Movie

bp = Blueprint('main', __name__, url_prefix='/')

model= joblib.load(open('flask_app/model.pkl', 'rb'))

@bp.route('/')
def hello():
    return render_template('User_list.html')

@bp.route('/value', methods=['GET','POST'])
def value():
    if request.method == 'POST':
        return render_template('home.html')

@bp.route('/predict', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        data1 = request.form.get('budget')
        data2 = request.form.get('runtime')
        data3 = request.form.get('vote_average')
        data4 = request.form.get('vote_count')
        data = [[data1, data2, data3, data4]]
        pred = model.predict(data)
        return render_template('predict.html', data=pred)



