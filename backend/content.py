import os

class Content:
    def __init__(self, name):
        self.name = name

    def path(self):
        return os.path.abspath(self.name)

    def get(self):
        if self.isfile():
            with open(self.path()) as f:
                return f.read()
        else:
            return os.listdir(self.path())

    def exists(self):
        return os.path.exists(self.path())

    def isdir(self):
        return os.path.isdir(self.path())
