import re
import requests
import time
import html

def waduanzi(page=1):
	url = 'http://www.waduanzi.com/page'+str(page)
	res = requests.get(url)
	#DIv
	div = re.compile("<div class=\"panel panel20 post-item post-box\">.*?<div class=\"item-content\">.*?</div>",re.S)
	body = html.escape(res.text).replace("<br/>","\n")
	m = div.findall(body)
	#user
	user = re.compile("<div class=\"post-author\".*?<a .*?>(.*?)</a>",re.S)
	title = re.compile("<h2 class=\"item-title\"><a.*?>(.*?)</a></h2>",re.S)
	#content
	content = re.compile("<div class=\"item-content\">(.*?)</div>",re.S)
	
	for joke in m:
		user1 = user.findall(joke)
		content1 = content.findall(joke)
		title1  = title.findall(joke)
		output = []
		if len(user1)>0:
			output.append(user1(0))
		if len(content1)>0:
			output.append(content1(0))
		if len(title1)>0:
			output.append(title1(0))
		print("\t".join(output))
	time.sleep(1)
if __name__ == '__main__':
	for i in range(1,10):
		waduanzi(i)
