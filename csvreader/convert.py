import csv

#Read the csv file stored in the folder
gameFile = open('top100.csv')

try:
	csvReader = csv.reader(gameFile)

	#List to store all of the read filedata in
	gameList = []

	#Read each row of the file and add to the list
	for row in csvReader:
		gameList.append(row)

	outputWriter = open('output.txt', 'w')

	#Go from end to start in the loop of list entries
	i = (len(gameList) - 1)

	while i >= 0:
		#The main content that will change depending on entry
		contentOut = '*' + gameList[i][0] + '. ' + gameList[i][1] + ' (' + gameList[i][2] + ')'

		outputWriter.write('<h2>' + '\n')
		outputWriter.write(contentOut + '\n')
		outputWriter.write('</h2>' + '\n')
		i = i-1

finally:
	gameFile.close()
	outputWriter.close()