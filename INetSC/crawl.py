from crawler.crawler import *
import threading
from queue import Queue
from general import *

base_url = ''
queue = Queue()


def create_workers(num_of_threads=8):
    for _ in range(num_of_threads):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        url = queue.get()
        Crawler.crawl_page(url)
        queue.task_done()


def create_jobs():
    queue_file = '{}/queue.txt'.format(base_url)
    queued_links = file_to_set(queue_file)
    if len(queued_links) > 0:
        for link in queued_links:
            queue.put(link)
        queue.join()
        create_jobs()


def crawl(url):
    global base_url
    base_url = get_tld(url)
    Crawler(url)
    create_workers()
    create_jobs()
