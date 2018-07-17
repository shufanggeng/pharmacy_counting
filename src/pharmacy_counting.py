import sys
import os
from operator import itemgetter

def sortDrugStats(stats):
	drugs = []
	for drug in stats.keys():
		drugs.append([drug, stats[drug]['users'], stats[drug]['total_cost']])
	sorted(drugs, key=itemgetter(2,1), reverse=True)
	return drugs

def updateUserSet(userSet, user):
	for u in userSet:
		if u['prescriber_first_name'] == user['prescriber_first_name'] and u['prescriber_last_name'] == user['prescriber_last_name']:
			return
	userSet += [user]

def processRow(stats, data):
	if data['drug_name'] in stats.keys():
		updateUserSet(stats[data['drug_name']]['users'],{'prescriber_first_name':data['prescriber_first_name'],'prescriber_last_name':data['prescriber_last_name']})
		stats[data['drug_name']]['total_cost'] = stats[data['drug_name']]['total_cost'] + int(data['drug_cost'])
	else:
		stats[data['drug_name']] = {'users':[{'prescriber_first_name':data['prescriber_first_name'],'prescriber_last_name':data['prescriber_last_name']}], 'total_cost': int(data['drug_cost'])}
#End processRow

def processStats(stats):
	for drug in stats.keys():
		stats[drug]['users'] = len(stats[drug]['users'])
#End processStats

def main():	
	#Read in command line arguments
	inputFileName=sys.argv[1]
	outputFileName=sys.argv[2]

	drugStats={}
	header=[]
	
	with open(inputFileName) as f:
		for rowId,entry in enumerate(f):
			entry = entry.rstrip().split(',')
			if rowId == 0:
				header = entry
			else:
				entry = dict(zip(header, entry))
				processRow(drugStats, entry)

	processStats(drugStats)
	
	with open(outputFileName,'w') as f:
		f.write('drug_name,num_prescriber,total_cost')
		drugStats = sortDrugStats(drugStats)
		for drug in drugStats:
			f.write(os.linesep + ','.join([drug[0],str(drug[1]),str(drug[2])]))
		
#End main

main()

exit(0)
