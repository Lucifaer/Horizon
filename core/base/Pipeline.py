from .Db import prepare, session


class Pipeline(object):
    def __init__(self):
        self.session = None

    def __enter__(self):
        prepare()
        self.session = session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        self.session = None
