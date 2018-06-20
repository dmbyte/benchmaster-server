#!/bin/bash
#need to get this from catcher
filename="7f730341-5f1b-328f-b3b2-efc2fcaedbbc"
uploadtime="20180418T004500"
testname="4M-seqread"
if [ $# -ne 1 ]; then
    echo "This script takes exactly 1 parameter, the .benchmark outputfile from benchmaster."
fi
#sed '/{/Q' $1 >temp.txt
echo { \"$filename\":[{\"uploadtime\":\"$uploadtime\"},{\"testname\":\"$testname\"}{ >$filename.json
sed -n '/{/,$ p' $1 >>$filename.json
python viewresult.py
echo }]} >>$filename.json
#rm temp.json

