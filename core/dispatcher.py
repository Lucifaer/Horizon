from .base.Config import Config
from .factory.createSpider import CreateSpider
from .factory.createPipeline import CreatePipeline
from pprint import pprint


class Dispatcher(object):
    def __init__(self, project):
        self.project = project
        self.config = Config(self.project)

    async def start(self):
        config = self.config.create_config()
        items, next_page = await CreateSpider(config).create_spider()
        pprint(items)
        pprint(next_page)
        # if items is not None:
        #     for i in items:
        #         i.setdefault('from', self.project)
        #         CreatePipeline.do_insert(i)
        # else:
        #     print("没有更新")
