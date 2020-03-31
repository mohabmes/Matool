import sys
from crawl import *
from scan import *


help = '''
python main.php [operation] [ref]

[operation]:
    scan            Scan website to get domain, nmap, robot file and whois info.
    crawl           Start Multi-threading crawling process.

[ref]:
    url             Any valid Website URL.
'''


def split_cmd():
    return sys.argv[1], sys.argv[2]


def abort(helper=1):
    print('\nFailed! :(')
    if helper == 1:
        print(help)
    exit()


def main():
    if sys.argv[1] == 'help':
        print(help)
    if len(sys.argv) == 3:
        operation, url = split_cmd()
        if (operation in ['scan', 'crawl']) & (len(url)>0):
            if operation == 'scan':
                try:
                    scan(url)
                    print('\nSuccessfully Done :)')
                except Exception as e:
                    print(e)
                    abort(0)
                return ''
            elif operation == 'crawl':
                try:
                    crawl(url)
                    print('Successfully Done :)')
                except Exception as e:
                    print(e)
                    abort(0)
                return ''
    abort()

main()
