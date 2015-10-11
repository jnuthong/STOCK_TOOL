# -*- encoding: utf-8 -*-
# author 	: jianbin.hong.cn@gmail.com
# date		: 2015/08/02

from os import listdir
import sys, json
from os.path import isfile, join


DIR = "/Users/hongjianbiny/Desktop/MyProject/personal_blog/downloads/PROXY"
INDUSTRY_DIR = DIR + "/dir_industries"
INDUSTRY_FILE = DIR + "/INDUSTRIES.LIST"
STOCK_INDEX_DIR = DIR + "/dir_finance_data"
STOCK_INDEX_HIST_DIR = DIR + "/dir_stock_history"

def func_get_files_under_dir(file_dir):
	"""
	"""
	pass

def func_stock_index_file_handle(file_path):
	"""
	This function will return a dictionary;
	"""
	date_index = []
	res = dict()
	with open(file_path, 'r') as file_obj:
		line_index = 0
		key = None
		for line in file_obj:
			line = line.strip("\n\r").split("\t")
			if line_index == 0:
				line_index += 1
				date_index = line
				continue

			for i in range(len(line)):
				if i == 0: 
					key = line[i]
					continue

				try:
					value = float(line[i])
				except Exception as e:
					value = 0

				if key not in res: res[key] = dict()
				res[key][date_index[i]] = value
	return res, set(date_index[1:])

def func_stock_index_detail_compute(file_path, time_set):
	"""
	"""
	res = dict()
	with open(file_path, 'r') as file_obj:
		for line in file_obj:
			line = line.strip("\n\r").split("\t")
			if line[0] in time_set: res[line[0]] = float(line[3])
	return res

def main():
	"""
	Main function extrance;
	- 1) get all of the industry catalog, and its stock indexs
	"""
	INDUSTRY_MAP = dict()
	with open(INDUSTRY_FILE, 'r') as file_obj:
		for line in file_obj:
			line = line.strip("\n\r").split("\t")
			INDUSTRY_MAP[line[0]] = [element for element in line[2].split(";") if len(element) != 0]

	condition = ["基本每股收益",
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

	for key, value in INDUSTRY_MAP.iteritems():

		print "[INFO]INDUSTRY_NAME: " + key
		print "[INFO]STOCK_INDEX_LIST: " + ",".join(value)
		industry_info = dict()
		TIME_SET = None
		for i in value:
			res, date_set = func_stock_index_file_handle(STOCK_INDEX_DIR + "/" + i)
			if TIME_SET is None: TIME_SET = date_set
			else: TIME_SET = TIME_SET.intersection(date_set)
			industry_info[i] = res

		TIME_SET = sorted([element for element in TIME_SET if len(element) != 0])

		print "[INFO]TIME_INDEX: " + "|".join(TIME_SET)
		for i in value:
			try:
				res_list = func_stock_index_detail_compute(STOCK_INDEX_HIST_DIR + "/" + i, TIME_SET)
				print res_list
			except Exception as e:
				continue

			ratio_data = ["0"]
			for j in range(1, len(TIME_SET)):
				try:
					ratio = (res_list[TIME_SET[i]] - res_list[TIME_SET[j - 1]]) / res_list[TIME_SET[j - 1]]
				except Exception as e:
					ratio = 0

				ratio_data.append(str(ratio))
			print "[INFO]STOCK_INDEX: " + i + " - " + "|".join(ratio_data)

		for factor in condition:
			res_list = []
			for date in TIME_SET:

				for key, value in industry_info.iteritems():
					if factor not in value: value[factor] = dict()
					if date not in value[factor]: 
						value[factor][date] = 0
						print "[WARN]INDEX : " + key + " - " + " DATE: " + date

				sorted_info = sorted(industry_info.items(), key=lambda x: x[1][factor][date], reverse=True)
				res_list.append(sorted_info)

			print "[INFO]FACTOR_NAME: " + factor
			print "[INFO]TIME_INDEX: " + "|".join(TIME_SET)
			for i in range(len(industry_info.keys())):
				tmp_res = ""
				for j in range(len(TIME_SET)):
					tmp_res += "STOCK_INDEX: " + res_list[j][i][0] + "-" + str(res_list[j][i][1][factor][TIME_SET[j]]) + " | "

				print tmp_res

		exit()
		print "########################## INDUSTRY SPLIT LINE ##########################"

if __name__ == "__main__":
	reload(sys)
	sys.setdefaultencoding("utf-8")
	main()