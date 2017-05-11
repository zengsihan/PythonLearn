# _*_ coding:utf-8 _*_


from urllib.request import urlopen

# 丑事百科的爬虫实验
# 20170425 zsh

page=1
url="http://www.qiushibaike.com/hot/page/"+str(page)
user_agent = "Mozilla/4.0(compatible;MSIE 5.5;Windows NT)"
headers={"User-Agant" : user_agent}
print("111")
try:
	print("22")
	request=Request(url,headers=headers)
	print("33")
	response=urlopen(request)
	print(response.read())
except  Exception as e:
	if hasattr(e,"code"):
		print(e.code)
	if hasattr(e,"reason"):
		print(e.reason)
