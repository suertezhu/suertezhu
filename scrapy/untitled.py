import requests

url = "http://www.qiushibaike.com/8hr/page/1"
res = requests.get(url)
print(res.text)