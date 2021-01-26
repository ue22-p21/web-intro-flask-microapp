from flask import Flask

def create_app():
    # ici __name__ vaut 'microapp'
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        return 'This is the homepage'

    return app
