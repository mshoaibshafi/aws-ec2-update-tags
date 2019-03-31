

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
			#print ("Tag_key > {} Tag_values >> {} Tag_values_list >> {} & line {}".format(Tag_key,Tag_values,Tag_values_list,line))
			#print (tag_keys_values)
			#input ("wait")
		return tag_keys_values
	#Tag_key = f.readlines().split('=')
	#print ("Tag_key {}".format(Tag_key))
	#print(f.read())




	# Uncomment below line if you want to use your own Tag Key values file
	# with open("tags.file.txt","r") as f:
