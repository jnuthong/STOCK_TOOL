# !/bin/bash
# author: jianbin.hong.cn@gmail.com
# date	: 2015/07/14

DIR=/vagrant/PROXY

start_year=2006
end_year=2015
diff=$(($end_year - $start_year))
# echo $diff
iterator_season="1 2 3 4"

if [ -f $DIR/STOCK_HIST_INPUT ];
then
	rm $DIR/STOCK_HIST_INPUT;
fi

touch $DIR/STOCK_HIST_INPUT;

while IFS='' read -r line; do
	# echo $line;
	for i in $(seq 1 $diff);
	do
		year=$(($i + $start_year));
		IFS=" " eval "array=($iterator_season)";
		for j in "${array[@]}";
		do
			echo -e $line"\t"$year"\t"$j >> $DIR/STOCK_HIST_INPUT;
		done
	done
done < $DIR/STOCK_SYMBOLS_INPUT