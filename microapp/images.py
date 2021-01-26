from itertools import chain
from pathlib import Path

ROOT = "microapp/static/images"

class Image:
    def __init__(self, path):
        self.path = path

    def url(self):
        return f"/static/images/{self.id}.png"

    # simuler un calcul server-side
    def area(self, x1, y1, x2, y2):
        return abs((x2-x1)*(y2-y1))

class Images:
    def __init__(self, root=ROOT):
        self.root = root

    def _scan(self):
        for image in Path(self.root).glob(f"*.png"):
            yield image

    def ids(self):
        for path in self._scan():
            yield path.stem

    def contents(self):
        for path in self._scan():
            yield Image(path)

    def locate(self, id):
        for path in self._scan():
            if path.stem == id:
                return Image(path)
