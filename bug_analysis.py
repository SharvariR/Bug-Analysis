import csv
import pandas as pd
import numpy as np

parent_occurrences = {}
leaf_nodes = []
internal_nodes = []

def main() :
	bug_report = pd.read_csv('bug_report.tsv', delimiter = '\t')
	bug_report = bug_report.replace(np.nan, 0, regex = True)
	for index,row in bug_report.iterrows() :
		parent_occurrences[row["parent_bug_id"]] = 0
		if row["occurrences"] != 0 :
			leaf_nodes.append(row["bug_id"])
			parent_occurrences[row["bug_id"]] = row["occurrences"]
		else :
			internal_nodes.append(row["bug_id"])
	result = build_tree(bug_report, parent_occurrences, leaf_nodes)

def analyze_occurrences(parent_occurrences, bug_report) :
	direct_affected_bugs = {}
	indirect_affected_bugs = {}
	print("\n####### ANALYSIS OF THE BUG REPORT #######")
	keyMax = max(parent_occurrences, key=parent_occurrences.get)
	keyValue = parent_occurrences[keyMax] 
	print("Alert :: Need to fix the bug with id %d , as it is most adundant bug with %d occurrences" %(int(keyMax), int(keyValue)))
	print("############################")
	print("Bugs affected due to this are : ")
	print("############################")
	print("\nDirectly affected bugs due to most abundant bug are :")
	for index,row in bug_report.iterrows() :
		if row["parent_bug_id"] == int(keyMax) :
			print("Description : " + row["bug_description"])
			direct_affected_bugs[row["bug_id"]] = row["percentage_contribution"]
	print("bug_id  contribution")
	for bug_id , contribution in direct_affected_bugs.items() : 
		print('{}         {}'.format(int(bug_id), int(contribution)))
	print("Indirectly affected bugs due to this are :\n")
	for index,row in bug_report.iterrows() :
		if row["parent_bug_id"] in direct_affected_bugs :
			print("Description : " + row["bug_description"])
			indirect_affected_bugs[row["bug_id"]] = row["percentage_contribution"]
	print("bug_id  contribution")
	for bug_id , contribution in indirect_affected_bugs.items() : 
		print('{}         {}'.format(int(bug_id), int(contribution)))
	print("############################")
	print("\nRespective effective occurrences are : ")
	print("bug_id  occurrences")
	for bug_id , occurrences in parent_occurrences.items() : 
		print('{}         {}'.format(int(bug_id), int(occurrences)))

def build_tree(bug_report, parent_occurrences, leaf_nodes) :
	parent_nodes = []
	for index,row in bug_report.iterrows() :
		if row["bug_id"] in leaf_nodes :
			parent_occurrences[row["parent_bug_id"]] = parent_occurrences[row["parent_bug_id"]]  + ((parent_occurrences[row["bug_id"]]* int(row["percentage_contribution"]))/ 100)
			parent_nodes.append(row["parent_bug_id"])
		else:
			continue
	if len(parent_nodes) != 1 :
		build_tree(bug_report, parent_occurrences, parent_nodes)
	else :
		analyze_occurrences(parent_occurrences, bug_report)

if __name__ == "__main__" :
	main()

