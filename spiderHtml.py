# encoding:UTF-8
import io
import sys
import re
import urllib
import urllib.request

req = {}
req['word'] = '陈浩'
url = "http://www.baidu.com/s?" + urllib.parse.urlencode(req)
data = urllib.request.urlopen(url).read().decode('UTF-8')
linkre = re.compile('href=\"(.+?)\"')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
for x in linkre.findall(data):
    if 'http' in x:
        print(x)
