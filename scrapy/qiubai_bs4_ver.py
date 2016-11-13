from bs4 import BeautifulSoup
import html5lib
import requests
def qiubaispi(page):

	url = "http://www.qiushibaike.com/pic/page/"+str(page)
	res = requests.get(url)
	soup = BeautifulSoup(res,html5lib)
	div_list = soup.find_all("div",class_="thumb")
	for div in div_list:
		img_list = div.find_all("img")
		for img in img_list:
			print(img)

if __name__ == '__main__':
	qiubaispi(1)