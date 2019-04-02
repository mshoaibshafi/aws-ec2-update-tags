# This program will list all tags of an ec2 instance and allow to add / update tags if needed

import boto3,sys
from pprint import pprint 
from extractTagKeysValues import extractTagKeysValues

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

# Data File : 
# Purpose : all the tags and their prospective values are in the file with a syntax "tag_name = tag_value1,tag_value2,tag_value3 ...."
# Filename : tags.file.txt or tags.file.txt.sample
# Process : Read all Tags from the file, split by "=" and then by "," and create a list
# For example :
# 	account = production,dev,qa
# 	output list :
# 	account = [production,dev,qa]


# Uncomment below line if you want to use your own Tag Key values file
Tag_Data_file = "tags.file.txt"				# Your own file not in Git
# Tag_Data_file = "tags.file.txt.sample"	# Included with Git

# TODO : Check if Tag_Data_file exist

Tag_Keys_Values = {}
# Call the function to extract Tags Key pair value from the tags.file.txt file
Tag_Keys_Values = extractTagKeysValues(Tag_Data_file)
#print (Tag_Keys_Values)

instanceTagDict = {}
for reservation in (response["Reservations"]):
	#pprint (reservation)
	for instance in reservation["Instances"]:
		# Grab the instance ID 
		# Clear the instanceTagDict before using it otherwise it will show wrong / old values 
		instanceTagDict.clear()
		pprint ("Instance ID  {}".format(instance["InstanceId"]))
		
		if "Tags" in instance: # If no Tags then skip to next instance			
			pprint ("Number of Tags {}".format(len(instance["Tags"])))
		else:
			pprint ("Number of Tags ZERO {}".format(instance["InstanceId"]))
			continue

		# print all Tags first
		print ("List of Tags from 6 Categories")

		for i in range(0,len(instance["Tags"])):
			instanceTagDict[instance["Tags"][i]['Key']] = instance["Tags"][i]['Value']

		pprint (instanceTagDict)
		# Check if account and environment tags are present then skip this instance 
		if ('account' in instanceTagDict.keys()) and ('environment' in instanceTagDict.keys()):
			print ("Skipping ... account and environment tags are present \n ")
			instanceTagDict.clear()
			continue

		resp = input ("\nDo you want to add Tags for this instance {}  ( y or yes ): ".format(instance["InstanceId"]))

		if resp.lower() == 'y' or resp.lower() == "yes":
			for k in Tag_Keys_Values.keys():
				print("Pick up a value for {} tag".format(k))
				for i in range(0,len(Tag_Keys_Values[k])):
					print ("{}: {}".format(i,Tag_Keys_Values[k][i]))
				print ("{}: {}".format(i+1,"skip"))
				resp_2 = int(input(": "))
				if resp_2 != i+1:
					ec2.create_tags(Resources=[instance["InstanceId"]], Tags=[{'Key':k, 'Value':Tag_Keys_Values[k][resp_2]}])
		else:
			# Clear the instanceTagDict before using it otherwise it will show wrong / old values 
			instanceTagDict.clear()
			continue

		input("Press Any Key to Continue ... \n")
