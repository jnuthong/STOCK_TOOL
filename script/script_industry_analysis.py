# -*- encoding:utf-8 -*-
# author	: jianbin.hong.cn@gmail.com
# date		: 2015/07/20

import sys, os, json, copy

# DIR_STOCK_FACTOR_PRO="/vagrant/PROXY/dir_finance_data/"

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

TIME_INFO = dict()

def main(file_dir, file_list, output):
	"""
	"""
	num_industry 	= len(file_list)
	default_dict 	= dict()
	time_index 		= None

	for x in FIRST_COLUMN:
		default_dict[x] = list()

	for element in file_list:
		# process file as element
		if len(element) == 0: continue
		print "[Info] Start File: " + element + " process..."
		if not os.path.isfile(file_dir + "/" + element):
			print "[Warn] Couldn't find File: " + file_dir + "/" + element
			continue

		line_index = 0
		with open(file_dir + "/" + element, 'r') as file_obj:
			for line in file_obj:
				line = line.strip("\r\n").split("\t")

				if line_index == 0: 
					time_index = line
				# process line as element
				for i in range(len(line)):

					if i == 0: continue
					if line_index == 0: 
						if line[i] not in TIME_INFO: TIME_INFO[line[i]] = copy.deepcopy(default_dict)

					if line_index > 0:
						key = FIRST_COLUMN[line_index]
						try:
							value = float(line[i])
						except Exception as e:
							# print line[i]
							value = 0
						# print time_index[i], key, value
						TIME_INFO[time_index[i]][key].append(value)

				line_index += 1
				# for key, value in TIME_INFO.iteritems():
				# 	print key
				# 	print json.dumps(value)
				# 	print "++++++++++++++++++++++++++++"

		print "[Info] Complete File: " + element + "."

	with open(output, 'w+') as file_obj:
		file_obj.write(json.dumps(TIME_INFO) + "\n")
	# print json.dumps(TIME_INFO)

if __name__ == "__main__":
	"""
	"""
	reload(sys)
	sys.setdefaultencoding("utf-8")

	file_dir  		= sys.argv[1]
	file_list 		= sys.argv[2].split(";")
	file_output 	= sys.argv[3]
	main(file_dir, file_list, file_output)