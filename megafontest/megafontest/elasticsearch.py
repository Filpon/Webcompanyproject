import json, datetime, requests
from time import sleep
from bs4 import BeautifulSoup
from haystack import site
from infonotesapi.models import Notes

class Elastic:
    try:
        r = requests.get(u, headers=headers)
        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, 'lxml')
            # title
            title_section = soup.select('firstHeading')

    except Exception as ex:
        print('Exception while parsing')
        print(str(ex))
    finally:
        return json.dumps(rec)

    if __name__ == '__main__':
        headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Pragma': 'no-cache'
    }
        url = 'https://ru.wikipedia.org/wiki/REST'
        r = requests.get(url, headers=headers)
    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        links = soup.select('firstHeading')
        for link in links:
            sleep(2)
            result = parse(link['href'])
            print(result)
            print('=================================')

class ElasticIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    links = indexes.CharField(model_attr='user')

    def get_model(self):
        return Notes

    def index_queryset(self, using=None):
        "Used when the entire index for model is updated."
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

site.register(Elastic, ElasticIndex)