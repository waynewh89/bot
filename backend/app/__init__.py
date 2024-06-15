from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from .routes import initialize_routes

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/solana_trading_bot'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    api = Api(app)
    initialize_routes(api)
    
    return app
