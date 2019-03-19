from core.base.Downloader import Downloader
from core.base.Selector import Selector
from pprint import pprint


class Spider(object):
    def __init__(self, config):
        self.config = config
        self.downloader = Downloader(self.config['spider']['start_url'])

    async def create_spider(self):
        if self.config['type'] == 'api':
            return await self.create_api_typed()
        elif self.config['type'] == 'page':
            return await self.create_next_page_typed()
        else:
            await self.create_next_page_typed()

    async def create_api_typed(self):
        pass

    async def create_next_page_typed(self):
        content = await self.downloader.http_request()
        item, next_page = Selector(self.config, content).get_data()
        pprint(item)
        pprint(next_page)
        # data, next_page = await self.selector.get_data(content)
        # return data, next_page

