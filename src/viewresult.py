#!/usr/bin/python
import json
with open('temp.json','r') as f:
	fiodata=json.load(f)
print 'Total Test Nodes: %s'% (len(fiodata['client_stats'])-1)
print 'RW Setting: %s'%(fiodata['client_stats'][0]['job options']['rw'])
print 'Read: %s'%(fiodata['client_stats'][0]['job options']['rwmixread'])
print 'IO Depth: %s'%(fiodata['client_stats'][0]['job options']['iodepth'])
print 'Jobs per node: %s'%(fiodata['client_stats'][0]['job options']['numjobs'])
print 'Latency Target: %s'%(fiodata['client_stats'][0]['job options']['latency_target'])
print 'Latency window %s'%(fiodata['client_stats'][0]['job options']['latency_window'])
print 'Percent of I/O that MUST be in the targer during the window: %s'%(fiodata['client_stats'][0]['job options']['latency_percentile'])
for x in range(0,len(fiodata['client_stats'])):
	print '-----------------------------------------------------------------------'
	if x == len(fiodata['client_stats'])-1:
		print 'SUMMARY STATS'
		print 'Write b/w:       %s MiB/s'% ((fiodata['client_stats'][x]['write']['bw'])/1024)
		print 'Write IOPS:      %s '% (fiodata['client_stats'][x]['write']['iops'])
		print 'Avg write lat:   %sms'% (fiodata['client_stats'][x]['write']['lat']['mean']/1000)
		print 'Max write lat:   %sms'% (fiodata['client_stats'][x]['write']['lat']['max']/1000)
		print 'STDev write:     %sms'% (fiodata['client_stats'][x]['write']['lat']['stddev']/1000)
		print ''
		print 'Read b/w:        %s MiB/s'% ((fiodata['client_stats'][x]['read']['bw'])/1024)
		print 'Read IOPS:       %s '% (fiodata['client_stats'][x]['read']['iops'])
		print 'Avg read lat:    %sms'% (fiodata['client_stats'][x]['read']['lat']['mean']/1000)
		print 'Max read lat:    %sms'% (fiodata['client_stats'][x]['read']['lat']['max']/1000)
		print 'STDev write:     %sms'% (fiodata['client_stats'][x]['read']['lat']['stddev']/1000)
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


