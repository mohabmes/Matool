from bs4 import BeautifulSoup
from urllib import parse


class ExtractLinks:
    base_url = ''
    page_url = ''
    links = set()

    def __init__(self, base_url, page_url):
        self.base_url = base_url
        self.page_url = page_url

    def extract_anchor(self, tags):
        soup = BeautifulSoup(tags, "html.parser")

        for link in soup.findAll("a"):
            href = link.get('href')
            if href[0:11] == 'javascript:' or href[0] == '#' or href[0:7] == 'mailto:':
                continue
            url = parse.urljoin(self.base_url, href)
            self.links.add(url.replace(' ', ''))

    def get_links(self):
        return self.links
