from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap








def create_app():
    app =Flask(__name__)
    


    app.config['SECRET_KEY'] = '123'
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://carolyne:1234@localhost/pitch-world'
    


    bootstrap = Bootstrap()
    db = SQLAlchemy()


    bootstrap.init_app(app)
    db.init_app(app)

  
  

    return app
