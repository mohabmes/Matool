# KADManga
Download your favorite Manga in a well-organized structure, without any extra effort and without navigating through pages. 
<br>**It stores the downloaded Mangas in saparate folders, each folder contains subfolders for each chapter.**

<br>**Note: [KADplus](https://github.com/mohabmes/KADplus) is the GUI version.**

## How to use
- First run it
> `Python KADManga.py`
- Download a certain chapter
`<url> <ChapterNum>`
> `http://www.mangareader.net/death-note   1`
- Download the whole Manga
`<url>`
> `http://www.mangareader.net/death-note`
- Download chapters by range
`<url> <start-index> <end-index>`
> `http://www.mangareader.net/death-note   4   10`

## Files Structure
├── Manga Name<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Chapter 1<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 1.jpg<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 2.jpg<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 3.jpg<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── ...<br>
└── ...<br>

## Dependencies
- BeautifulSoup4
- tld

## Tested on
- Windows 10
- Ubuntu 16

## Support
- mangareader.net
- mangapanda.com


<br>For any suggestion email me on [mohab.elsheikh@gmail.com](mailto:mohab.elsheikh@gmail.com).

<br>Feel free to use it.
