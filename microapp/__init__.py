from flask import Flask

from .views import image_view, images_view, image_api_area

def create_app():
    # ici __name__ vaut 'microapp'
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        return images_view()

    @app.route('/image/<id>')
    def image(id):
        return image_view(id)

    @app.route('/api/image/area/<id>/<x1>/<y1>/<x2>/<y2>')
    def image_area(id, x1, y1, x2, y2):
        args = (float(x) for x in (x1, y1, x2, y2))
        return image_api_area(id, *args)

    return app
