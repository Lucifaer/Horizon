from .Filter import Filter
from bs4 import BeautifulSoup
from lxml import etree
from pprint import pprint


class Selector(object):
    def __init__(self, config, content):
        self.rules = config['spider']['rules']
        self.selector = etree.HTML(content)
        self.content = content
        self.filter = Filter(config['spider']['start_url'])

    def get_data(self):
        items = dict()
        for k, v in self.rules.items():
            items.setdefault(k, self.selector.xpath(v))
        item, next_page = self.item_relationship(items, today=True)
        return item, next_page

    def item_relationship(self, items, **kwargs):
        item = []
        for i in range(len(items['title_link'])):
            try:
                info_collections = {
                    'title': self.filter.handle_title(items['title_link'][i].text),
                    'link': self.filter.handle_url(items['title_link'][i].attrib.get('href')),
                    'tag': items['tag'][i].text,
                    'date': self.filter.handle_date(items['date'][i]),
                }
            except IndexError as tag_err:
                info_collections = {
                    'title': self.filter.handle_title(items['title_link'][i].text),
                    'link': self.filter.handle_url(items['title_link'][i].attrib.get('href')),
                    'tag': '未知',
                    'date': self.filter.handle_date(items['date'][i].text),
                }
            item.append(info_collections)
        try:
            next_page = self.filter.handle_url(items['next_page'][0].attrib.get('href'))
            pprint(next_page)
        except IndexError as next_page_err:
            next_page = None
        return item, next_page

    def test(self):
        items = dict()
        for k, v in self.rules.items():
            pprint(k)
            pprint(v)
            pprint(self.soup.select(v))
