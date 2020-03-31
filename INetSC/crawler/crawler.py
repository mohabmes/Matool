import requests
from .ExtractLinks import *
from .generate_file import *
from general import *
from tld import get_tld
from scanner.domain import *

class Crawler:

    project_name = ''
    url = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, url):
        Crawler.project_name = get_tld(url)
        Crawler.url = url
        Crawler.queue_file = Crawler.project_name + '/queue.txt'
        Crawler.crawled_file = Crawler.project_name + '/crawled.txt'
        # self.queue.add(url)
        self.boot()
        self.crawl_page(Crawler.url)


    @staticmethod
    def boot():
        create_dir(Crawler.project_name)
        generate_files(Crawler.url)
        Crawler.queue = file_to_set(Crawler.queue_file)
        Crawler.crawled = file_to_set(Crawler.crawled_file)


    @staticmethod
    def crawl_page(page_url):
        if page_url not in Crawler.crawled:
            print('crawling ' + page_url)
            print('Queue ' + str(len(Crawler.queue)) + ' | Crawled  ' + str(len(Crawler.crawled)))
            Crawler.add_links_to_queue(Crawler.gather_links(page_url))
            Crawler.queue.remove(page_url)
            Crawler.crawled.add(page_url)
            Crawler.update_files()


    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = requests.get(page_url, allow_redirects=True)
            html_string = response.text.encode('ascii', 'replace')
            finder = ExtractLinks(Crawler.url, page_url)
            finder.extract_anchor(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.get_links()


    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Crawler.queue) or (url in Crawler.crawled):
                continue
            if Crawler.project_name not in get_domain_name(url):
                continue
            Crawler.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Crawler.queue, Crawler.queue_file)
        set_to_file(Crawler.crawled, Crawler.crawled_file)
