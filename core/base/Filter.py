from pprint import pprint
from datetime import datetime, timedelta


class Filter(object):
    def __init__(self, main_url):
        self.main_url = main_url

    @staticmethod
    def translate_word(word):
        table = {ord(f): ord(t) for f, t in zip(
            u'，。！？：【】（）/％＃＠＆１２３４５６７８９０',
            u',.!?:[]()-%#@&1234567890'
        )}
        return word.translate(table)

    def handle_title(self, title):
        word = title.strip()
        return self.translate_word(word)

    def handle_url(self, short_url):
        full_links = list()
        param_dict = (self.main_url + short_url).split('/')
        for i in param_dict:
            if i not in full_links:
                if i != '':
                    full_links.append(i)
        protocol = full_links.pop(0)
        return protocol + "//" + '/'.join(full_links)

    @staticmethod
    def handle_tag(tag):
        pass

    @staticmethod
    def handle_date(date):
        now = datetime.now()
        temp_date = date.strip().split(' ')
        trimed_date = ''
        if len(temp_date) > 1:
            temp_date.pop(0)
            time_describe = temp_date.pop(0).split('\xa0')
            if time_describe[-1] == 'minutes' or time_describe[-1] == 'an' or time_describe[-1] == 'hours':
                trimed_date = now.strftime('%Y-%m-%d')
            elif time_describe[-1] == 'day':
                trimed_date = (now - timedelta(days=1)).strftime('%Y-%m-%d')
            elif time_describe[-1] == 'days':
                trimed_date = (now - timedelta(days=int(time_describe[0]))).strftime('%Y-%m-%d')
            else:
                trimed_date = time_describe.pop()
        elif len(temp_date) == 0:
            trimed_date = temp_date.pop()
        else:
            trimed_date = temp_date.pop()
        return trimed_date


# if __name__ == '__main__':
    # main_url_list = [
    #     'https://sec.today/pulses/',
    #     'https://xz.aliyun.com/',
    #     'https://paper.seebug.org/'
    # ]
    # short_url = [
    #     '/pulses/81255b1a-cf4c-452e-a4f8-77d4c2128901/',
    #     '/t/4420',
    #     '/862/'
    # ]
    # for i in range(len(main_url_list)):
    #     pprint(short_url[i] + "split like this:")
    #     test = Filter(main_url_list[i])
    #     test.handle_url(short_url[i])
    #     pprint("====================")
    # date_list = [
    #     '• 51\xa0minutes ago',
    #     '• 1\xa0day ago',
    #     '• 2\xa0days ago',
    #     ' / 2019-03-20\n    ',
    #     '2019-03-20'
    # ]
    # for i in date_list:
    #     test = Filter('test')
    #     test.handle_date(i)
    #     pprint("====================")
