import os

#Finds all the file name occurencies in the dir
def find_in(dir, fileName):
	results = []

	for root, dirs, files in os.walk(dir):
		for file in files:
			#Split the filename to get the file extension
			split = file.split('/')
			fName = split[len(split)-1]

			#If the filename is the desired name, get it
			if (fName == fileName):
				results.append(os.path.join(root, file))

	return results

#Finds all the files in dir with the extension
def find_in_ext(dir, extension = ""):
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

#Same as _ext(), but removes the path up to dir
def find_in_ext_relative(dir, extension = ""):
	results = []

	for root, dirs, files in os.walk(dir):
		root = str(root).replace(dir, "")
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
