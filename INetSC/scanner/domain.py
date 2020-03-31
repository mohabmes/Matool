from tld import get_tld
from socket import gethostbyname


def get_domain_name(url):
    domain = get_tld(url)
    return domain


def get_ip_address(url):
    url = get_domain_name(url)
    return gethostbyname(url)