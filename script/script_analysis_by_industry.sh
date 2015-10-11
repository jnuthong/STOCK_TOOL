# author 	: jianbin.hong.cn@gmail.com
# dat		: 2015/07/20

DIR_INDUSTRY_DATA=$(dirname $(pwd))/dir_industries
DIR_STOCK_FACTOR_PRO=$(dirname $(pwd))/dir_finance_data
INDUSTRY_LIST=$(dirname $(pwd))/INDUSTRIES.LIST

STOCK_SYMBOLS_INPUT=$(dirname $(pwd))/STOCK_SYMBOLS_INPUT
DIR_INDUSTRY_OUTPUT=/vagrant/PROXY/dir_industries

# if [ -f $STOCK_SYMBOLS_INPUT ];
# then
# 	rm $STOCK_SYMBOLS_INPUT;
# fi

# while read -r line;
# do
# 	IFS=$'\t' array=($line)
# 	list="${array[2]}";
# 	# echo "${array[1]}", $list;
# 	IFS=";" brray=($list);
# 	# 1) base on the given industry name, we want to compute the following factor:
# 	# 			- average price in this industry, as well as standard derivation;
# 	#			- average Price/Earning ratio in this industry, as well as standard derivation;
# 	#			- average 1/Earning ratio in this industry, as well as std derivation;
# 	# 			- Book Value Per Share;

# 	# python script_industry_analysis.py $DIR_STOCK_FACTOR_PRO "$list" > ../tmp.data
# 	for i in "${brray[@]}";
# 	do
# 		echo $i >> $STOCK_SYMBOLS_INPUT;
# 	done
# 	# exit
# done < $INDUSTRY_LIST

while read -r line;
do
	IFS=$'\t' array=($line)
	list="${array[2]}";
	# echo "${array[1]}", $list;
	IFS=";" brray=($list);
	# 1) base on the given industry name, we want to compute the following factor:
	# 			- average price in this industry, as well as standard derivation;
	#			- average Price/Earning ratio in this industry, as well as standard derivation;
	#			- average 1/Earning ratio in this industry, as well as std derivation;
	# 			- Book Value Per Share;
	catalog="${array[1]}"
	python script_industry_analysis.py $DIR_STOCK_FACTOR_PRO "$list" $DIR_INDUSTRY_OUTPUT/$catalog
done < $INDUSTRY_LIST