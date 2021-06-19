from flask import Flask
from .config import Config
from flask_bootstrap import Bootstrap

boostrap = Bootstrap()

def create_app(config=Config):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    boostrap.init_app(app)

    from .main import main
    app.register_blueprint(main)

    from .auth import auth
    app.register_blueprint(auth)

    return app