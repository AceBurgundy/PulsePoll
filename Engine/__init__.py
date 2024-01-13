from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask import Flask

db = SQLAlchemy()
socketio = SocketIO()

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = "02acf27fea4d3asdasdfasfde325232345wetg4qbg43c002a063da2e71cf56e866be904fd5467670b99efa8a5d035a1"
    app.config['SESSION_TYPE'] = "filesystem"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    db.init_app(app)
    socketio.init_app(app)

    from Engine.index.views import index
    from Engine.candidate.views import candidate
    from Engine.errors.handlers import errors

    app.register_blueprint(index)
    app.register_blueprint(candidate)
    app.register_blueprint(errors)

    return app
