#JSON Merger

'''
Utility which takes bunch of JSON files as input
which contains JSON arrays,
and writes them as a single array in new JSON file.
Maximum size of the output can also be specified.

'''
import os
wordlist=[]
def changedirectory():
	'''
	Takes path from the end user and changes
	current working directory to that path.
	In case of invalid directory, asks user
	to enter a valid directory
	
	TIME COMPLEXITY for this function = O(1) [checks directory exist or not]
	SPACE COMPLEXITY for this function = O(1)

	'''
	print("Enter directory path:")
	print('Example: /home/username/Desktop')
	correctdircheck=1
	while(correctdircheck):
		path=input()
		if(os.path.exists(path)):
			os.chdir(path)
			#print(os.getcwd())
			print("Directory changed to "+path)
			correctdircheck=0
		else:
			print('Enter a valid directory')
			print('Example: /home/username/Desktop')
	return 1

def readfiles():
	'''
	Gets input file base name from the user.
	starts from [filename]1.json and increases till
	last file. splits the file and appends it to
	global list.

	TIME COMPLEXITY for this function = O(n*m) ["n" for 
										no.of.files, "m" for no.of.words in files]
	SPACE COMPLEXITY for this function = O(m)
	'''
	print('Enter Base name of input json file:')
	input_file_basename=input()
	current_file_value=1
	while(os.path.exists(input_file_basename+str(current_file_value)+'.json')):
		filename=input_file_basename+str(current_file_value)+'.json'
		file=open(filename,'r')
		for eachline in file:
			wordlist.extend(eachline.strip().split(','))
		file.close()
		current_file_value+=1
	return 1
def writetofiles():
	'''
	Checks for already available output file.
	Incase if it finds one, increments and the count
	value and searches for next file in that folder.
	Creates a new file with write mode and
	line buffering policy when it fails to find one.

	'''
	print('Enter Base name of output json file:')
	output_file_basename=input()
	print('Enter Max size of the file to be created in BYTES.')
	max_size=int(input())
	current_file_value=1
	while(os.path.exists(output_file_basename+str(current_file_value)+'.json')):
		current_file_value+=1
	outfilename=output_file_basename+str(current_file_value)+'.json'
	outputfilecontent = open(outfilename,'w+',1)
	'''
	loops through the global list and appends
	JSON keywords to the output file.
	TIME COMPLEXITY = O(n) ["n" is the size of world list]

	'''

	outputfilecontent.write(wordlist[0]+'\n')
	counter=1
	for element in range(1,len(wordlist)):
		if wordlist[element]!=wordlist[0] and wordlist[element]!='' and wordlist[element]!=wordlist[-1] and (os.stat(outfilename).st_size+50)<max_size:
			if counter&1:
				outputfilecontent.write('\n')
				outputfilecontent.write('	')
			outputfilecontent.write(wordlist[element]+',')
			counter+=1
	outputfilecontent.write('\n'+wordlist[-1])
	'''
	If file size increases the MAX_SIZE it gets truncated.
	and reports on successful completion.

	'''
	if(os.stat(outfilename).st_size)>max_size:
		print(outfilename+' file Writing stopped in the middle due to MAX SIZE constraint but')
		print(str(max_size)+' bytes size intermediate file will be created in your folder.')
		print('Please try increasing size')
		outputfilecontent.close()
	else:
		print(outfilename+' got successfully created in your path!')
		outputfilecontent.close()
	return 1

def main():
	changedirectory()
	readfiles()
	writetofiles()

main()