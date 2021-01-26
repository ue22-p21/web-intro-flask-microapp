from itertools import chain
from pathlib import Path

ROOT = "microapp/static/images"

class Image:
    """
    not very smart for now, but could be the entry point
    for writing sophisticated features, e.g. using opencv
    """
    def __init__(self, path):
        self.path = path

    def area(self, x1, y1, x2, y2):
        """
        simulate a server-side computation
        """
        return abs((x2-x1)*(y2-y1))

class Images:
    """
    acts as an index of the available images
    based on the contents of the images/folder
    """
    def __init__(self, root=ROOT):
        self.root = root

    def _scan_paths(self):
        """
        an iterable of Path instances
        """
        return Path(self.root).glob(f"*.png")

    def ids(self):
        """
        list the ids found in the folder
        """
        return [path.stem for path in self._scan_paths()]

    def locate(self, id):
        """
        return an Image instance if that id was found
        None otherwise
        """
        for path in self._scan_paths():
            if path.stem == id:
                return Image(path)
