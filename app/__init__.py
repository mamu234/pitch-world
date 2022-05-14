from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap




db = SQLAlchemy()


def create_app():
    app =Flask(__name__)


    app.config['SECRET_KEY'] = '123'
    app.config['SQLALCHEMY_DATABASE_URI']=''
    
    bootstrap = Bootstrap(app)   
 


    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User , Pitch

  


    return app
