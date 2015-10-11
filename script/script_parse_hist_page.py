# -*- coding: utf-8 -*-
# author : jianbin.hong.cn@gmail.com
# date	: 2015/07/12

from bs4 import BeautifulSoup
import sys
sys.path.append("/Library/Python/2.7/site-packages")
import sys, os, requests, re

def get_page(stock_index, year, season):
	"""
	ref: http://money.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/600000.phtml?year=2014&jidu=4
	"""
	BASE_URL = "http://money.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/%s.phtml?year=%s&jidu=%s" % (stock_index, year, season)
	return requests.get(BASE_URL)

if __name__ == "__main__":

	reload(sys)
	sys.setdefaultencoding("utf-8")

	with open(sys.argv[1], 'r') as file_obj:
		content = BeautifulSoup(file_obj)

		table 	= content.findAll("table", {"id": "FundHoldSharesTable"})
		if len(table) == 0:
			# this may cause data-missing
			exit()
		rows = table[0].findAll("tr")
		for row in rows:
			res = ""
			columns = row.findAll("td")

			column_index = 0
			for column in columns:
				# print re.sub('\s+', '', column.text)
				res += re.sub('\s+', '', column.text) + "\t"

			if len(res) == 0: continue
			print res.encode("utf-8")