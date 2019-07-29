import os

from frater.utilities.singleton import Singleton


class FileStore(metaclass=Singleton):
    def __init__(self, root):
        self.root = os.path.abspath(os.path.expandvars(os.path.expanduser(root)))

    def get_full_path(self, image_path):
        full_path = os.path.join(self.root, image_path)
        return full_path
