from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import requests
import os
import errno
import sys

def show_msg(contect):
    msg.showinfo("Information", contect)

def show_warn(contect):
    msg.showwarning("Warning", contect)

try:
    from bs4 import BeautifulSoup
    from tld import get_tld
except:
    show_warn('Both \'tld\' and \'bs4\' are required to run this App')
    sys.exit(0)



def download_image(url, name, dirc=None, ch=None):
    try:
        req = requests.get(url)
    except:
        show_warn("Connection Error")
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
    try:
        resp = requests.get(url, allow_redirects=False)
    except:
        show_warn('An error occurred. Something wrong with the URL.')
        sys.exit(0)

    src_code = resp.text.encode('ascii', 'replace')
    bs = BeautifulSoup(src_code, "html.parser")
    return bs



def get_domain_name(url):
    domain = get_tld(url, fix_protocol=True)
    return domain


def extract_chapter(url):
    domain_name = get_domain_name(url)
    chapters = []
    titles = []
    soup = get_markup(url)
    all_chapter = soup.find("table", {"id": "listing"})
    try:
        for ch in all_chapter.findAll('a'):
            chapters.append("http://www."+domain_name + ch.get('href') + "/")
            titles.append(ch.text)
    except:
        show_warn('Invalid URL')

    return chapters, titles


def get_chapter_count(url):
    soup = get_markup(url)
    count = soup.find("select", {"id": "pageMenu"}).next_sibling.split()[-1]
    return int(count)


def get_chapter_img(url):
    soup = get_markup(url)
    img_url = soup.find("img", {"id": "img"})
    return img_url.get('src')


def download_chapter(url, dirc=None, ch=None):
    if url[-1] != '/':
        url += '/'
    count = get_chapter_count(url)
    print(count)
    for i in range(1, count+1):
        print("Downloading ({}/{}) ... ".format(i, count))
        status.config(text="Downloading ({}/{}) ... ".format(i, count))
        img_url = url + str(i)
        img_src = get_chapter_img(img_url)
        download_image(img_src, str(i), dirc, ch)


def download_manga(url, start=None, end=None):
    if url[:7] != "http://":
        url = "http://" + url
    try:
        domain_name = get_domain_name(url)
    except:
        show_warn('Invalid URL')
        # sys.exit(0)

    if domain_name == "mangareader.net" or domain_name == "mangapanda.com":
        chapters, titles = extract_chapter(url)
        dirc = url.split("/")[-1]
        show_msg("Might take a while, depending on your Internet connection speed.")
        if start is (None or "") and end is (None or ""):
            start = 0
            end = len(chapters)

        elif start is not (None or "") and end is (None or ""):
            if start < len(chapters):
                start -= 1
                end = start + 1
            else:
                show_warn('Check the Start index.')
                # sys.exit(0)
        elif start is not (None or "") and end is not (None or ""):
            start -= 1
            if not (start < len(chapters) and end-1 < len(chapters) and start < end-1):
                show_warn('Check the Start & end indices.')
                # sys.exit(0)

        for i in range(start, end):
            print("Working on '{}' ({})".format(titles[i], chapters[i]))
            download_chapter(chapters[i], dirc, titles[i])

        print("Done")
    else:
        show_warn("Not supported Website")

def init(url, s=None, e=None):
    if url is not (None or ""):
        if s is not "":
            s = int(s)
        if e is not "":
            e = int(e)

        download_manga(url, s, e)
    else:
        show_warn("URL field is empty!")


root = Tk()
root.resizable(0,0)
root.geometry("600x320")
root.title("KADManga 1.0")

lbl_title = Label(root, text="KADManga")
lbl_url = Label(root, text="URL:")
txt_url = Entry(root, width=65, font=('arial', 10))


lbl_index= Label(root, text="Index")
lbl_from = Label(root, text="from:")
txt_from = Entry(root)
lbl_to = Label(root, text="to:")
txt_to = Entry(root)

pb = ttk.Progressbar(root, orient="horizontal", length=470, mode="determinate")
btn = Button(root, text="Download", command=lambda: init(txt_url.get(), txt_from.get(), txt_to.get()))

status = Label(root, text="Ready", bd=1, relief=SUNKEN, anchor=W, width=85)

lbl_title.grid(row=0, column=0, padx=12, pady=12)
lbl_url.grid(row=1, column=0, padx=5, pady=12)
txt_url.grid(row=1, column=1, padx=12, pady=12)

lbl_index.grid(row=4, column=0, padx=2, pady=2)
lbl_from.grid(row=5, column=0)
txt_from.grid(row=5, column=1, padx=5, pady=5, sticky=W)
lbl_to.grid(row=6, column=0)
txt_to.grid(row=6, column=1, padx=5, pady=5, sticky=W)

pb.grid(row=10, column=1, padx=0, pady=5, sticky=W)
btn.grid(row=9, column=1, ipadx=20, ipady=5, pady=20, sticky=W)
status.grid(row=11, sticky=NW, pady=20, columnspan=3)

root.mainloop()
