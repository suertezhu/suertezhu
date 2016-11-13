import re
import requests

def crawl_image(img_url,path):
	img = requests.get(img_url,stream=True)
	with open(path,'wb') as f:
		f.write(img.content)


def taonv_spider(page=1):
	url = "https://mm.taobao.com/141234233.htm?spm=719.1001036.1998606008."+str(page)+".BDqQYJ"
	res = requests.get(url)
	
	div_list = re.findall("<div class=\"mm-aixiu-content\" id=\"J_ScaleImg\">(.*?)</div>",res.content.decode("GBK"),re.S)
	for div in div_list:
		img_list = re.findall("<img.*?src=\"(.*?)\"",div)
		for img_url in img_list:
			crawl_image(img_url,"./images/"+img_url.split("/")[-1])

if __name__ == '__main__':
	for i in range(1,3):
		taonv_spider(i)