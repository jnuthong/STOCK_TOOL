# author: jianbin.hong.cn@gmail.com
# date	: 2015/07/12

# Function implement in this script:
#	1) get the finance analysis data from website: http://stockpage.10jqka.com.cn/600299/finance/
#		- get the website info base on the given stock index; ref: http://basic.10jqka.com.cn/600299/xls/mainreport.xls
#		- parse the website and store and format easy use data format;

DIR=$(dirname $(pwd))
SCRIPT_DIR=$(pwd)
DATA_DIR=$DIR/dir_original_finance_data
DATA_PRO_DIR=$DIR/dir_finance_data
SH_STOCK_INDEX=$DIR/SH_STOCK_SYMBOLS
SZ_STOCK_INDEX=$DIR/SZ_STOCK_SYMBOLS
STOCK_SYMBOLS_INPUT=$DIR/STOCK_SYMBOLS_INPUT
# source $DIR/GET_FREE_PROXY.sh # this script is used to get the whole current online stock index 

echo $SH_STOCK_INDEX

func_generate_url(){
	stock_index=$1;
	echo "http://basic.10jqka.com.cn/$stock_index/xls/mainreport.xls";
}

while IFS='' read -r line || [[ -n $line ]]; do 
	res=$(func_generate_url $line);
	wget $res -O $DATA_DIR/"$line.xls";
	/usr/bin/py_xls2html $DATA_DIR/"$line.xls" > $DIR/tmp.data
	# sed -i "s/\"\\u/u\"\\u/" $DIR/tmp.data
	python $SCRIPT_DIR/script_parse_page.py $DIR/tmp.data > $DATA_PRO_DIR/$line
done < $STOCK_SYMBOLS_INPUT

exit

# while IFS='' read -r line || [[ -n $line ]]; do 
# 	res=$(func_generate_url $line);
# 	# echo $res
# 	wget $res -O $DATA_DIR/"$line.xls";
# 	/usr/bin/py_xls2html $DATA_DIR/"$line.xls" > $DIR/tmp.data
# 	# sed -i "s/\"\\u/u\"\\u/" $DIR/tmp.data
# 	python $SCRIPT_DIR/script_parse_page.py $DIR/tmp.data > $DATA_PRO_DIR/$line
# done < $SH_STOCK_INDEX


# while IFS='' read -r line || [[ -n $line ]]; do 
# 	res=$(func_generate_url $line);
# 	# echo $res
# 	wget $res -O $DATA_DIR/"$line.xls";
# 	/usr/bin/py_xls2html $DATA_DIR/"$line.xls" > $DIR/tmp.data
# 	# sed -i "s/\"\\u/u\"\\u/" $DIR/tmp.data
# 	python $SCRIPT_DIR/script_parse_page.py $DIR/tmp.data > $DATA_PRO_DIR/$line
# done < $SZ_STOCK_INDEX

