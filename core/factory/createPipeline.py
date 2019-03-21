from core.base.Pipeline import Pipeline
from modules import info_store


class CreatePipeline(object):
    def __init__(self):
        pass

    @staticmethod
    def do_insert(item):
        session = Pipeline()
        with session as s:
            if not s.query(info_store.Table.link).filter(info_store.Table.link == item['link']).first():
                data = info_store.Table(
                    title=item['title'],
                    link=item['link'],
                    tag=item['tag'],
                    publish_date=item['date']
                )
                s.add(data)
                s.commit()
