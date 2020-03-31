import io
import urllib.request


def get_robots_file(url):
    if not url.endswith('/'):
        url += '/'
    url += 'robots.txt'
    req = urllib.request.urlopen(url, data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()