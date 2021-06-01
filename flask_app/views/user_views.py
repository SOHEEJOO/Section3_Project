from flask import Blueprint, render_template, request, jsonify
from flask.wrappers import Request
from flask_app.models import User
import joblib

bp = Blueprint('User', __name__, url_prefix='/user')



@bp.route('/list')
def list():
    User_list=User.query.order_by(User.id.desc())
    return render_template('User_list.html', User_list = User_list)

@bp.route('/detail/<int:User_id>')
def detail(User_id):
    User2 = User.query.get(User_id)
    return render_template('User_detail.html', User = User2)





