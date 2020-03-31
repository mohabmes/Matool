from general import *
from tld import get_tld


def generate_files(url):
    name = get_tld(url)
    path = '{}/{}.txt'

    create_dir(name)

    queue = path.format(name, 'queue')
    crawled = path.format(name, 'crawled')

    if not os.path.isfile(queue):
        write_file(queue, url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# generate_files('https://google.com')
# delete_file('google.com/queue.txt')