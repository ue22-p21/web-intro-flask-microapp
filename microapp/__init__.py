from flask import Flask

from .views import index_view, image_view, images_view, image_api_area

def create_app():
    # ici __name__ vaut 'microapp'
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        return index_view()

    @app.route('/image/')
    @app.route('/image/<id>')
    def image(id=None):
        if not id:
            return images_view()
        else:
            return image_view(id)

    return app
