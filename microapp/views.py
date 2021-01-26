from flask import Flask, render_template

from .images import Image, Images

def index_view():
    return render_template("index.html")

def images_view():
    images = Images()
    return render_template("images.html", ids=images.ids())

def image_view(id):
    images = Images()
    image = images.locate(id)
    return render_template("image.html", id=id, image=image)

def image_api_area(id, x1, y1, x2, y2):
    pass
