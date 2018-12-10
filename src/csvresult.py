#!/usr/bin/python
import json
import sys
testname=sys.argv[1]
#print '*******TEST NAME: %s *******' %(testname)
with open('temp.json','r') as f:
	fiodata=json.load(f)
#print 'Total Test Nodes: %s'% (len(fiodata['client_stats'])-1)
rwsetting=fiodata['client_stats'][0]['job options']['rw']
readpercentage=fiodata['client_stats'][0]['job options']['rwmixread']
maxiodepth=fiodata['client_stats'][0]['job options']['iodepth']
jobspernode=fiodata['client_stats'][0]['job options']['numjobs']
if 'latency_target' in fiodata['client_stats'][0]['job options']:
	lattarget=fiodata['client_stats'][0]['job options']['latency_target']
	latwindow=fiodata['client_stats'][0]['job options']['latency_window']
	latpercentage=fiodata['client_stats'][0]['job options']['latency_percentile']
else:
	lattarget=0
	latwindow=0
	latpercentage=0
for x in range(0,len(fiodata['client_stats'])):
	if x == len(fiodata['client_stats'])-1:
		writebw=fiodata['client_stats'][x]['write']['bw']/1024
		writeiops=fiodata['client_stats'][x]['write']['iops']
		writeavglat=fiodata['client_stats'][x]['write']['lat']['mean']/1000
		writemaxlat=fiodata['client_stats'][x]['write']['lat']['max']/1000
		readbw=fiodata['client_stats'][x]['read']['bw']/1024
		readiops=fiodata['client_stats'][x]['read']['iops']
		readavglat=fiodata['client_stats'][x]['read']['lat']['mean']/1000
		readmaxlat=fiodata['client_stats'][x]['read']['lat']['max']/1000
		print '"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s"'% (testname,rwsetting,readpercentage,maxiodepth,jobspernode,lattarget,latwindow,latpercentage,writebw,writeiops,writeavglat,writemaxlat,readbw,readiops,readavglat,readmaxlat)
		#print 'Write b/w:       %s MiB/s'% ((fiodata['client_stats'][x]['write']['bw'])/1024)
		#print 'Write IOPS:      %s '% (fiodata['client_stats'][x]['write']['bw'])
		#print 'Avg write lat:   %sms'% (fiodata['client_stats'][x]['write']['lat']['mean']/1000)
		#print 'Max write lat:   %sms'% (fiodata['client_stats'][x]['write']['lat']['max']/1000)
		#print 'STDev write:     %sms'% (fiodata['client_stats'][x]['write']['lat']['stddev']/1000)
		#print ''
		#print 'Read b/w:        %s MiB/s'% ((fiodata['client_stats'][x]['read']['bw'])/1024)
		#print 'Read IOPS:       %s '% (fiodata['client_stats'][x]['read']['bw'])
		#print 'Avg read lat:    %sms'% (fiodata['client_stats'][x]['read']['lat']['mean']/1000)
		#print 'Max read lat:    %sms'% (fiodata['client_stats'][x]['read']['lat']['max']/1000)
		#print 'STDev write:     %sms'% (fiodata['client_stats'][x]['read']['lat']['stddev']/1000)
#	else:
# removed so it only prints summary data
		#print 'Hostname:  %s'% (fiodata['client_stats'][x]['hostname'])
#	print 'Write b/w:       %s MiB/s'% ((fiodata['client_stats'][x]['write']['bw'])/1024)
#	print 'Write IOPS:      %s '% (fiodata['client_stats'][x]['write']['bw'])
#	print 'Avg write lat:   %sms'% (fiodata['client_stats'][x]['write']['lat']['mean']/1000)
#	print 'Max write lat:   %sms'% (fiodata['client_stats'][x]['write']['lat']['max']/1000)
#	print 'STDev write:     %sms'% (fiodata['client_stats'][x]['write']['lat']['stddev']/1000)
#	print ''
#	print 'Read b/w:        %s MiB/s'% ((fiodata['client_stats'][x]['read']['bw'])/1024)
#	print 'Read IOPS:       %s '% (fiodata['client_stats'][x]['read']['bw'])
#	print 'Avg read lat:    %sms'% (fiodata['client_stats'][x]['read']['lat']['mean']/1000)
#	print 'Max read lat:    %sms'% (fiodata['client_stats'][x]['read']['lat']['max']/1000)
#	print 'STDev write:     %sms'% (fiodata['client_stats'][x]['read']['lat']['stddev']/1000)
