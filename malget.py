#/usr/bin/python

# Note : This is for python3
# install requests lib if not installed

import requests
import json
import os

banner = """

MM    MM         lll   GGGG         tt    
MMM  MMM   aa aa lll  GG  GG   eee  tt    
MM MM MM  aa aaa lll GG      ee   e tttt  
MM    MM aa  aaa lll GG   GG eeeee  tt    
MM    MM  aaa aa lll  GGGGGG  eeeee  tttt
				
				-- By Himanshu Khokhar (@rinne_parad0x)
"""

url_api 	= "https://dasmalwerk.eu/api"				# To list latest malwares from Das Malwerk
url_malware = "http://dasmalwerk.eu/zippedMalware/"


def saveMalware(malName):
	print("Saving file : " + malName + " ...")

	malware = requests.get(url_malware + malName)
	
	with open(malName + ".zip" , "wb") as mal:
		mal.write(malware.content)

	print("Malware has been saved as : " + malName + "\n")



def obtainMalware():
	print(banner)


	details = requests.get(url_api)


	# Get JSON data from response
	jsonData = details.text


	# Convert JSON data to Python Dictionary for processing
	data = json.loads(jsonData)

	# Dictionary has one key - items - and it has all the details
	data = data['items']

	# Obtain the no. of malwares in response. Sub 1 because the last value is - {'debug': 'no'}
	num = len(data) - 1 

	print("List of samples : ")

	for i in range(0, num):
		print("%02d.) %s" %(i + 1, data[i]['Hashvalue']))	

	choice = int(input("\nChoose the index value or 0 to download all the samples : "))

	choice  = choice - 1

	#	All the malware samples will be saved under Samples dir in the directory of script
	#
	#	If you want to change, change the variable - sample

	sample = os.path.join(os.getcwd(), "Samples")

	if os.path.isdir(sample) is False:
		os.mkdir(sample)

	os.chdir(sample)

	if choice == -1:

		print("Downloading all samples ... \n")
		
		for i in range(0, num):
			malName = data[i]['Filename'] + ".zip"
			saveMalware(malName)
	
	elif choice >= 0 and choice < len(data):

		malName = data[choice]['Filename'] + ".zip"		
		print("Downloading " + malName + "\n")

		saveMalware(malName)

	else:
		print("Choose a valid choice.")
		os._exit(1)


	print("Note : The password of the zip file is - infected")
	print("\nEnjoy malware analysis.")


if __name__ == '__main__':
	obtainMalware()