import re
import requests

def crawl_image(img_url,save_path):
	img = requests.get(img_url,stream=True)
	with open(save_path,'wb') as f:
		f.write(img.content)

def images_spider(page=1):
	url = "http://www.qiushibaike.com/imgrank/page/"+str(page)
	res = requests.get(url)
	div_list = re.findall("<div class=\"thumb\">(.*?)</div>",res.content.decode("utf-8"),re.S)
	
	for div in div_list:
		img_list = re.findall("<img src=\"(.*?)\"",div)
		for img_url in img_list:
			crawl_image(img_url,'./images/'+img_url.split('/')[-1])

if __name__ == '__main__':
	for i in range(1,10):
		images_spider(i)

