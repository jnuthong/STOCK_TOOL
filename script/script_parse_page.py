# -*- encoding: utf-8 -*-
# author : jianbin.hong.cn@gmail.com
# date	: 2015/07/12

from bs4 import BeautifulSoup
import sys, os

FIRST_COLUMN = ["科目\时间",
				"基本每股收益",
				"净利润",
				"净利润同比增长率",
				"营业总收入",
				"营业总收入同比增长率",
				"每股净资产",
				"净资产收益率",
				"净资产收益率-摊薄",
				"资产负债比率",
				"每股资本公积金",
				"每股未分配利润",
				"每股经营现金流",
				"销售毛利率",
				"存货周转率"]

if __name__ == "__main__":
	
	reload(sys)
	sys.setdefaultencoding("utf-8")

	with open(sys.argv[1], 'r') as file_obj:
		content = BeautifulSoup(file_obj)

		rows = content.findAll("tr")

		row_index = 0
		for row in rows:
			res = ""
			columns = row.findAll("td")

			column_index = 0
			for column in columns:
				if column_index == 0:
					if len(FIRST_COLUMN) == row_index + 1: 
						exit()
					res += FIRST_COLUMN[row_index] + "\t"
					row_index += 1
					column_index += 1
				else:
					try:
						res += eval(column.text) + "\t"
					except Exception as e:
						None

			print res