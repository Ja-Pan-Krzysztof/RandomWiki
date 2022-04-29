import requests
from threading import Thread
from requests.exceptions import HTTPError
import console_args
import sys


class RandomWiki:
    def __init__(self, lang):
        self.code = lang
        self.url = 'https://en.wikipedia.org/wiki/'
        try:
            self.site = requests.get(
                url=self.url,
            )
            self.site.encoding = 'utf-8'
            self.site.raise_for_status()

        except HTTPError as http_error:
            print(f'HTTP error occurred : {http_error}')
            sys.exit()

        except Exception as exception:
            print(f'Other error occurred : {exception}')
            sys.exit()

        else:
            print('Success !')

    def _how_many(self):
        site = f'https://{self.code}.wikipedia.org/wiki/Special:Random'
        try:
            url = requests.get(
                url=site
            )
        except TimeoutError as timeout_error:
            print(f'Timeout Error : {timeout_error}')

        else:
            with open('links/links.txt', 'a') as f:
                f.write(f'{url.url}\n')

            print(url.url)

    def random_wiki_pl(self, many: int):
        if many > 1:
            while many != 0:
                t = Thread(target=self._how_many)
                t.start()

                many -= 1

        else:
            self._how_many()


if __name__ == '__main__':
    code = console_args.main().Language
    count = console_args.main().Count

    r = RandomWiki(lang=code)
    r.random_wiki_pl(many=count)



