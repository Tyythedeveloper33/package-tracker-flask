from flask import Flask
from app.config import Configuration
from app.routes import bp
from app.model import db
from flask_migrate import Migrate
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Configuration)
    app.register_blueprint(bp)

    db.init_app(app)
    migrate.init_app(app, db)
    return app

app = create_app()

