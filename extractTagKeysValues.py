

import sys


def extractTagKeysValues(file):
	tag_keys_values = {}
	with open(file,"r") as f:
		for line in f.readlines(): 
			# Get the Key name
			Tag_key = line.strip().split('=')[0].strip()
			# Get the Key Values in list
			Tag_values = line.strip().split('=')[1]
			Tag_values_list = Tag_values.strip().split(',')

			# Insert the Key Value Pair in the Dictionary
			tag_keys_values[Tag_key] = Tag_values_list
		return tag_keys_values
	


