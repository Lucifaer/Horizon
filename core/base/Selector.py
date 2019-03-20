from bs4 import BeautifulSoup
from lxml import etree
from pprint import pprint


class Selector(object):
    def __init__(self, config, content):
        self.rules = config['spider']['rules']
        self.url = config['spider']['start_url']
        self.selector = etree.HTML(content)
        self.content = content

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
                    'title': self.translate_word(items['title_link'][i].text),
                    'link': self.create_full_links(items['title_link'][i].attrib.get('href')),
                    'tag': items['tag'][i].text,
                    'date': items['date'][i],
                }
            except IndexError as tag_err:
                info_collections = {
                    'title': self.translate_word(items['title_link'][i].text),
                    'link': self.create_full_links(items['title_link'][i].attrib.get('href')),
                    'tag': '未知',
                    'date': items['date'][i].text,
                }
            item.append(info_collections)
        pprint(item)
        try:
            next_page = self.create_full_links(items['next_page'][0])
        except IndexError as next_page_err:
            pprint(next_page_err)
            next_page = None
        return item, next_page

    @staticmethod
    def translate_word(word):
        table = {ord(f): ord(t) for f, t in zip(
            u'，。！？：【】（）/％＃＠＆１２３４５６７８９０',
            u',.!?:[]()-%#@&1234567890'
        )}
        return word.translate(table)

    def create_full_links(self, short_tag):
        full_links = ''
        link_dict = (self.url + short_tag).split('/')
        for i in range(len(link_dict)):
            if link_dict[i] != '':
                full_links += link_dict[i]
            else:
                if i == 1:
                    full_links += '//'
                else:
                    full_links += '/'
        return full_links

    def test(self):
        items = dict()
        for k, v in self.rules.items():
            pprint(k)
            pprint(v)
            pprint(self.soup.select(v))
