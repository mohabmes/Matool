# INetSC
INetSC is a tool used to **Crawl** &amp; **Scan** (domain, nmap, robot file and whois info) Websites.

## How to use
- to scan `python main.php scan <url>`
> `python main.php scan https://example.com`
- to crawl `python main.php crawl <url>`
> `python main.php crawl https://example.com`
- or type `help`
```
python main.php [operation] [ref]

[operation]:
    scan            Scan website to get domain, nmap, robot file and whois info.
    crawl           Start Multi-threading crawling process.

[ref]:
    url             Any valid Website URL.
```

## Dependencies
- pythonwhois
- nmap
- bs4
- tld

## Tested on
- Windows 10

<br>For any suggestion email me on [mohab.elsheikh@gmail.com](mailto:mohab.elsheikh@gmail.com).
