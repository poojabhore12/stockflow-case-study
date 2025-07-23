from flask import Flask
from app.utils.db import db
from app.routes.products import products_bp
from app.routes.alerts import alerts_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stockflow.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(products_bp)
    app.register_blueprint(alerts_bp)

    return app
