# -*- encoding: utf-8 -*-
# author : jianbin.hong.cn@gmail.com
# date	: 2015/07/12

import sys, json

if __name__ == "__main__":
	
	reload(sys)
	sys.setdefaultencoding("utf-8")

	with open(sys.argv[1], 'r') as file_obj:
		obj = json.load(file_obj)
		if "data" in obj:
			for element in obj["data"]:
				res = ""
				if "platename" in element: res += element["platename"] + "\t"
				else: res += "\t"

				if "hycode" in element: res+= element["hycode"]
				else: res += "\t"

				print res.encode("utf-8")
