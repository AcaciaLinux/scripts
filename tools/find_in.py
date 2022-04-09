import os

def find_in(dir, extension = ""):
	results = []

	for root, dirs, files in os.walk(dir):
		for file in files:
			#Split the filename to get the file extension
			split = file.split('.')
			fType = split[len(split)-1]

			#If the extension indicates the wanted extension, add it
			if (extension == ""):
				results.append(os.path.join(root, file))
			elif (fType == extension):
				results.append(os.path.join(root, file))

	return results
