import os

from flask import Flask


def create_app(config=None):
    # create and configure flask app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    return app