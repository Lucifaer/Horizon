from json import load


class Config(object):
    def __init__(self, file_name):
        self.file = "./config/" + file_name + ".json"

    def create_config(self):
        with open(self.file, 'r') as f:
            item = load(f)
        config = self.parse_config(item)
        return config

    @staticmethod
    def parse_config(item):
        config = dict()
        for k, v in item.items():
            config.setdefault(k, v)
        return config
