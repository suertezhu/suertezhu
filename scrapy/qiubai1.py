from bs4 import BeautifulSoup
import requests
import html5lib
import time
def parser(page=1):
	url = "http://www.qiushibaike.com/8hr/page/"+str(page)
	res = requests.get(url)
	soup = BeautifulSoup(res.text,html5lib)
	joke_list = soup.find_all('div',class_="article block untagged mb15")
	for child in joke_list:
		print(child.find('h2').string +"/t"+''.join(child.find('div',class_="content")).string)
	time.sleep(1)
if __name__ == '__main__':
	parser()