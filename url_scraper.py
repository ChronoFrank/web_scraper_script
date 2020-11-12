import re
import urllib.request
from  urllib.error import HTTPError, URLError
from collections import Counter


def request_to_url(url=None):
    if url:
        req = urllib.request.Request(
            url,
            data=None,
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4)"
                             " AppleWebKit/537.36 (KHTML, like Gecko)"
                             " Chrome/83.0.4103.97 Safari/537.36"}
        )
        try:
            response = urllib.request.urlopen(req)
            raw_data = response.read().decode('utf-8')
            return raw_data
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)


def extract_html_tags(data=''):
    regex = r'(<\/[a-z]*>)'
    tags_dict = dict()
    result = re.findall(regex, data)
    if result:
        total_elements = len(list(set(result)))
        tags_dict['total_elements'] = total_elements
        top_five = Counter(result).most_common(5)
        tags_dict['top_five'] = dict()
        for item_tuple in top_five:
            if item_tuple:
                tags_dict['top_five'].update({item_tuple[0]: item_tuple[1]})

        return tags_dict

if __name__ == '__main__':
    given_url = input("enter url to scrape -> ")
    print("url to analise -> {0}".format(given_url))
    data = request_to_url(given_url)
    result_dict = extract_html_tags(data)
    print("total elements in the webpage -> {0}".format(result_dict.get('total_elements')))
    print("top 5 most frequently used tags -> {0}".format(result_dict.get('top_five')))