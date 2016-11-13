import time
import re
import html
import requests

def QBspider(page=1):
    url = 'http://www.qiushibaike.com/8hr/page/'+str(page)
    res = requests.get(url)
    #爬取DIV
    div = re.compile("<div class=\"article block untagged mb15\".*?<div class=\"content\">.*?</a>",re.S)
    body = html.unescape(res.text).replace("<br/>","\n")
    m = div.findall(body)
    #爬取USER
    user = re.compile("<div class=\"author clearfix\".*?<h2>(.*?)</h2>",re.S)
    #爬取段子
    content = re.compile("<div class=\"content\"(.*?)</div>",re.S)
    for joke in m:
        username = user.findall(joke)
        contentt = content.findall(joke)
        output = []
        if len(username)>0:
	        output.append(username[0])
	        
        if len(contentt)>0:
	        output.append(contentt[0])

        print("\t".join(output))
    time.sleep(1)
if __name__ == '__main__':
    for i in range(1,10):
        QBspider(i)









