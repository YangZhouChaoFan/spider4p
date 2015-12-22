import re
import urllib
import urllib.request
import html.parser
import random
import os


class MyParser(html.parser.HTMLParser):
    def __init__(self):
        self.flag = False
        html.parser.HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'a' and self.flag == False:
            for name, value in attrs:
                if name == 'class' and value == 'previous-comment-page':
                    self.flag = True
                if name == 'href' and self.flag == True:
                    self.url = value

    def getUrl(self):
        return self.url


headers = {'User-Agent': 'IE'}
downloadHeaders = {
    'mine-type': 'application/x-msdownload',
    'User-Agent': 'IE'
}
url = "http://jandan.net/ooxx"
num = 1
while (num <= 20):
    print("pageNo: " + str(num))
    req = urllib.request.Request(url=url, headers=headers)
    data = urllib.request.urlopen(req).read().decode('UTF-8')
    linkre = re.compile('href=\"(.+?)\"')
    for link in linkre.findall(data):
        if 'http' in link and ('jpg' in link or 'gif' in link):
            if not os.path.exists('download'):
                os.mkdir('download')
            dowloadReq = urllib.request.Request(url=link, headers=downloadHeaders)
            filename = 'download/' + link[link.rindex("/") + 1:]
            fp = open(filename, "wb+")
            file = urllib.request.urlopen(dowloadReq).read()
            fp.write(file)
            fp.close()
            print(filename)
    mp = MyParser()
    mp.feed(data)
    url = mp.getUrl() + "&r=" + str(random.random())
    num = num + 1
