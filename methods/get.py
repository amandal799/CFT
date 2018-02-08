
def getData(url,params=None):
	'''
		This is the function which directly talks to the 
		codeForces API for extracting information.

		This is basically an intermediator between codeForces
		API and other functions of this project which processes 
		the data extracted.
	'''
	
	# importing required modules
	import requests
	
	# Extracting information
	try:
		if params is None:
			response = requests.get(url)
			return response
		else:
			response = requests.get(url,params)
			return response
	except Exception as e:
		return None
	
def getDic(response):
	'''
		This function converts the extracted information into
		a dictionary.
	'''
	# importing required modules
	import json
	try:
		return json.loads(response.content.decode('utf-8'))
	except Exception:
		return None
		
