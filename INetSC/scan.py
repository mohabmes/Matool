from scanner.whois import *
from scanner.robot_info import *
from scanner.domain import *
from scanner.nmap import *
from general import *


def write_report(domain_name, ip_address, robots_file, whois):

    create_dir(domain_name)

    echo('domain name')
    write_file(gname(domain_name, 'domain_name'), domain_name)
    echo('ip address')
    write_file(gname(domain_name, 'ip_address'), ip_address)
    echo('robots file')
    write_file(gname(domain_name, 'robots_file'), robots_file)
    echo('whois')
    write_file(gname(domain_name, 'whois'), whois)


def scan(url):
    domain_name = get_tld(url)
    ip_address = get_ip_address(url)
    robots_file = get_robots_file(url)
    whois = get_whois(domain_name)

    write_report(domain_name, ip_address, robots_file, whois)


def gname(domain_name, filename):
    return "{}/{}.txt".format(domain_name, filename)


def echo(str):
    print("scanning for {} ... ".format(str))
