from flask import Flask, render_template
import json

# here we could also write
# from microapp.model import ...
from .model import Image, Images

def images_view():
    images = Images()
    return render_template("images.html", ids=images.ids())

def image_view(id):
    images = Images()
    image = images.locate(id)
    return render_template("image.html", id=id, image=image)

def image_api_area(id, x1, y1, x2, y2):
    result = {'area': Image(id).area(x1, y1, x2, y2)}
    return json.dumps(result)
