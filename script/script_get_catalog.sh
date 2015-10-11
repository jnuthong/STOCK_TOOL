# !/bin/bash
# author : jianbin.hong.cn@gmail.com
# date	: 2015/07/12

# this script is used to get current industry category in the china stock market;
# it does following thing
#	- 1) get the whole category index;
#	- 2) 

DIR=$(dirname $(pwd))
TMP_DIR=$DIR/tmp
SCRIPT_DIR=$(pwd)
DATA_DIR=$DIR/dir_original_finance_data
DATA_PRO_DIR=$DIR/dir_finance_data
DATA_IND_DIR=$DIR/dir_industries

# curl http://q.10jqka.com.cn/interface/stock/thshy/zdf/desc/1/quote/quote > $DIR/json.data
# python script_parse_json.py $DIR/json.data > $DIR/INDUSTRIES
# curl http://q.10jqka.com.cn/interface/stock/thshy/zdf/desc/2/quote/quote > $DIR/json.data
# python script_parse_json.py $DIR/json.data >> $DIR/INDUSTRIES

# ref: http://q.10jqka.com.cn/stock/thshy/swzp/

# $DIR/INDUSTRIES.LIST
# store the industry \t industry hycode \t industry stock index code
if [ -f $DIR/INDUSTRIES.LIST ];
then
	rm $DIR/INDUSTRIES.LIST
fi

while IFS='' read -r line || [[ -n $line ]]; do 
	IFS="\t" eval "array=($line)";
	echo "${array[1]}"
	catalog="${array[1]}"
	name="${array[0]}"
	curl "http://q.10jqka.com.cn/stock/thshy/$catalog/" > $TMP_DIR/website.catalog.data
	iconv -f gbk -t utf-8 $TMP_DIR/website.catalog.data > $TMP_DIR/website.catalog.data.utf-8
	python $SCRIPT_DIR/script_get_catalog_list.py $TMP_DIR/website.catalog.data.utf-8 $catalog $name >> $DIR/INDUSTRIES.LIST
done < $DIR/INDUSTRIES