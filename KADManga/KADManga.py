import requests
import os
import errno
import sys

try:
    from bs4 import BeautifulSoup
    from tld import get_tld
except:
    print('tld, bs4 required !!')
    sys.exit(0)


sys.tracebacklimit = None


# Create directory
def create_dir(dirc):
    if not os.path.exists(dirc):
        os.makedirs(dirc)


def download_image(url, name, dirc=None, ch=None):
    """
        download single image, name it. put it in the chapter directory.
        Handle directory creation (Manga) & sub-directory (Chapter) and file naming (image).

        Parameters
        ----------
        url : string
            Direct url to the image
        name : string
            Name of the image (num)
        dirc : string
            Directory name
        ch  : string
            Chapter name
    """
    try:
        req = requests.get(url)
    except:
        print("Connection Error")
    if dirc is not None:
        filename = dirc + "/" + ch + "/" + name + ".jpg"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        f = open(filename, 'wb')
        for chunk in req.iter_content(128):
            f.write(chunk)
    else:
        f = open(name + ".jpg", 'wb')
        for chunk in req.iter_content(128):
            f.write(chunk)


def get_markup(url):
    """
        Get HTML code of certain page.

        Parameters
        ----------
        url : string

        Returns
        ----------
        Parsed HTNL BeautifulSoup object
    """
    try:
        resp = requests.get(url, allow_redirects=False)
    except:
        print('An error occurred. Something wrong with the URL.')
        sys.exit(0)

    src_code = resp.text.encode('ascii', 'replace')
    bs = BeautifulSoup(src_code, "html.parser")
    return bs



def get_domain_name(url):
    """
        Get Top level domain.

        Parameters
        ----------
        url : string

        Returns
        ----------
        domain name
    """
    domain = get_tld(url, fix_protocol=True)
    return domain


def extract_chapter(url):
    """
        extract all the Manga's chapters (url & name).

        Parameters
        ----------
        url : string
            url of certain Manga

        Returns
        ----------
        chapters : array
            array contain the chapters' URL
        titles : array
            array contain the chapters' title
    """
    domain_name = get_domain_name(url)
    chapters = []
    titles = []
    soup = get_markup(url)
    all_chapter = soup.find("table", {"id": "listing"})
    try:
        for ch in all_chapter.findAll('a'):
            chapters.append("http://www."+domain_name + ch.get('href') + "/")
            titles.append(ch.text)
            # print(domain_name + ch.get('href') + " : " + ch.text)
    except:
        print('Invalid URL')

    return chapters, titles


def get_chapter_count(url):
    """
        count of the images in certain chapter.

        Parameters
        ----------
        url : string
            url of certain chapter

        Returns
        ----------
        count : int
    """
    soup = get_markup(url)
    count = soup.find("select", {"id": "pageMenu"}).next_sibling.split()[-1]
    return int(count)


def get_chapter_img(url):
    """
        Extract src of image from the page.

        Parameters
        ----------
        url : string
            url of certain part in a chapter

        Returns
        ----------
        img_url : string
            source location of an image
    """
    soup = get_markup(url)
    img_url = soup.find("img", {"id": "img"})
    return img_url.get('src')


def download_chapter(url, dirc=None, ch=None):
    """
        Navigating throw all chapter's part to Download it (one by one).

        Parameters
        ----------
        url : string
            url of certain chapter
        dirc : string
            Directory name
        ch : string
            Chapter name
    """
    if url[-1] != '/':
        url += '/'
    count = get_chapter_count(url)
    print(count)
    for i in range(1, count+1):
        print("Downloading ({}/{}) ... ".format(i, count))
        img_url = url + str(i)
        img_src = get_chapter_img(img_url)
        download_image(img_src, str(i), dirc, ch)


def download_manga(url, start=None, end=None):
    """
        Check the page & supported websites.
        Handle sub-directory naming.
        Download starting & ending point.
        Navigating throw all chapter's part to Download it.

        Parameters
        ----------
        url : string
            url of certain chapter
        start : int
            starting index (chapter) [Default is zero]
        end : int
            ending index (chapter) [Default is the chapter len]


        Returns
        ----------
        img_url : string
            source location of an image
    """
    if url[:7] != "http://":
        url = "http://" + url
    try:
        domain_name = get_domain_name(url)
    except:
        print('Invalid URL')
        sys.exit(0)

    if domain_name == "mangareader.net" or domain_name == "mangapanda.com":
        chapters, titles = extract_chapter(url)

        # cut the manga name off the url
        dirc = url.split("/")[-1]
        print("Might take a while, depending on your Internet connection speed.")

        # to download the whole series
        if start is None and end is None:
            start = 0
            end = len(chapters)
        # to download only one chapter
        elif start is not None and end is None:
            # exceed the chapters count
            if start < len(chapters):
                start -= 1
                end = start + 1
            else:
                print('Check the Start index.')
                sys.exit(0)
        # to download by start & end index
        elif start is not None and end is not None:
            start -= 1
            if not (start < len(chapters) and end-1 < len(chapters) and start < end-1):
                print('Check the Start & end indices.')
                sys.exit(0)

        for i in range(start, end):
            print("Working on '{}' ({})".format(titles[i], chapters[i]))
            download_chapter(chapters[i], dirc, titles[i])

        print("Done")
    else:
        print("Not supported Website")


# Handle Slicing the command
def cmd_slice(str):
    cmd = str.split()
    s = None
    e = None

    if len(cmd) >= 3:
        e = int(cmd[2])
    if len(cmd) >= 2:
        s = int(cmd[1])
    if len(cmd) >= 1:
        url = cmd[0]
    return url, s, e


def init():
    while(True):
        cmd = input(">> ")
        try:
            url, s, e = cmd_slice(cmd)
        except:
            print("Incorrect Format")
            continue
        download_manga(url, s, e)


init()
