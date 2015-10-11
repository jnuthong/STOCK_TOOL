# !/bin/bash
# author: jianbin.hong.cn@gmail.com
# date	: 2015/07/14

DIR=/vagrant/PROXY
DATA_DIR=$DIR/dir_stock_history
SCRIPT_DIR=$DIR/script
TMP_DATA_DIR=$DIR/tmp

# 1) generate the following format data:
# 	- $stock_index \t year \t season;
# sh $SCRIPT_DIR/script_generate_stock_input_hist.sh
# ref: http://money.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/600000.phtml?year=2014&jidu=4

files=($DATA_DIR/*)
if [ ${#files[@]} -gt 0 ];
then
	echo "Delete all the files in directory: $DATA_DIR"
	rm $DATA_DIR/*
fi

while IFS='' read -r line || [[ -n $line ]];
do
	IFS=' ' eval "array=($line)";
	stock_index="${array[0]}";
	year="${array[1]}";
	season="${array[2]}";
	echo $stock_index, $year, $season, "$TMP_DATA_DIR/stock_hist.data.$stock_index.$year.$season"
	# curl -Ls -o $TMP_DATA_DIR/stock_hist.data.$stock_index.$year.$season http://money.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/$stock_index.phtml?year=$year&jidu=$season
	iconv -c -f gbk -t utf-8 "$TMP_DATA_DIR/stock_hist.data.$stock_index.$year.$season" > "$TMP_DATA_DIR/stock_hist.data.utf-8"
	
	if [ ! -f $DATA_DIR/$stock_index ];then
		touch $DATA_DIR/$stock_index;
	fi

	python $SCRIPT_DIR/script_parse_hist_page.py $TMP_DATA_DIR/stock_hist.data.utf-8 >> $DATA_DIR/$stock_index
done < $DIR/STOCK_HIST_INPUT