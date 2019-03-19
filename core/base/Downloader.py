from pyppeteer import launch
import aiohttp
from pprint import pprint


class Downloader(object):
    def __init__(self, url):
        self.url = url

    async def headless_request(self):
        try:
            browser = await launch()
            page = await browser.newPage()
            await page.goto(self.url, {'waitUntil': 'networkidle2'})
            return await page.content()
        except Exception as exc:
            pprint(exc)
        finally:
            await browser.close()

    async def http_request(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xm…ml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0'
        }
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(self.url) as response:
                    return await response.text()
        except Exception as exc:
            pprint(exc)
