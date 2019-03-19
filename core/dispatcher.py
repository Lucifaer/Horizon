from .base.Config import Config
from .factory.createSpider import Spider


class Dispatcher(object):
    def __init__(self, project):
        self.project = project
        self.config = Config(self.project)

    async def start(self):
        config = self.config.create_config()
        await Spider(config).create_spider()
