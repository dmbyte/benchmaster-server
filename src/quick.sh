#!/bin/bash
#need to get this from catcher
if [ $# -ne 1 ]; then
    echo "This script takes exactly 1 parameter, the .benchmark outputfile from benchmaster."
fi
echo '"testname","rwsetting","readpercentage","maxiodepth","jobspernode","lattarget","latwindow","latpercentage","writebw","writeiops","writeavglat","writemaxlat","readbw","readiops","readavglat","readmaxlat"'
for i in `find $1 -name *.benchmark`
do 
	#sed '/{/Q' $1 >temp.txt
	char="/"
	count=`awk -F"${char}" '{print NF-1}' <<< "${i}"`
	count2=$((count))
	testname=`echo $i|cut -f $count2 -d $char `
	sed -n '/{/,$ p' $i >temp.json
	python csvresult.py $testname
	#read -r -p 'press enter to continue' p
	rm temp.json
done

