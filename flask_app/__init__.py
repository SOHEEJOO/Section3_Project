from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    #ORM(db와 migrate함수를 create_app 함수 밖에서 생성하고 안에서 객체초기화 수행)
    db.init_app(app)
    migrate.init_app(app, db)

    #models에서 생성한 모델들을 플라스크의 migrate 기능이 인식할 수 있도록!
    #models에서 user와 answer 모델을 추가했으므로 데이터베이스가 변경되도록 'flask db migrate'
    from . import models

    #블루프린트
    from .views import main_views, user_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(user_views.bp)


    return app

if __name__ == '__main__':
    app.run()