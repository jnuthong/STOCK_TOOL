# -*- encoding: utf-8 -*-
# author : jianbin.hong.cn@gmail.com
# date	: 2015/07/12

import sys, json, re,requests
from bs4 import BeautifulSoup

# ref: http://q.10jqka.com.cn/interface/stock/detail/zdf/desc/2/1/fdckf

def extrance(num, hycode, name):
	"""
	"""
	text=""
	for i in range(1, num+1):
		url="http://q.10jqka.com.cn/interface/stock/detail/zdf/desc/%s/%s/%s" % (str(i), str(1), hycode)
		# print url
		res = requests.get(url)
		obj  = json.loads(res.text)
		if "data" in obj:
			for element in obj["data"]:
				if "stockcode" in element:
					text+=element["stockcode"]+";"

	res = name + "\t" + hycode + "\t" + text
	print res.encode("utf-8")

if __name__ == "__main__":
	
	reload(sys)
	sys.setdefaultencoding("utf-8")

	hycode 	= sys.argv[2]
	name 	= sys.argv[3] 

	with open(sys.argv[1], 'r') as file_obj:
		content = BeautifulSoup(file_obj)

		info = content.findAll("span", {"class": "page_info"})
		if len(info) == 0:
			exit()

		# print info[0].text
		num = re.findall(r"\/\d+", info[0].text)

		if len(num) == 0:
			exit()

		num = int(num[0][1:])
		extrance(num, hycode, name)