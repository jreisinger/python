#!/usr/bin/python

def get_links(url):
    import requests
    from bs4 import BeautifulSoup as soup
    result = requests.get(url)
    page = result.text
    doc = soup(page, "lxml")
    links = [element.get('href') for element in doc.find_all('a')]
    return links

if __name__ == '__main__':
    import sys, os
    if len(sys.argv) < 2:
        print "Usage:", sys.argv[0], "url [url2...]"
        os._exit(1)
    for url in sys.argv[1:]:
        print '--> links in', url
        for num, link in enumerate(get_links(url), start=1):
            print "%02d %s" % (num, link)
        print
