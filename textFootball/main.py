#start out by importing team list and simulate tournament
#list scores for each round
#split teams at true random and generate results at true random

import random
import time
import teamStore

def runTournament(teamList):
	#run the tournament overall

	while len(teamList) > 1:
		
		roundName = getRoundName(len(teamList))
		print '~~~' + roundName + '~~~'
	
    		#split into brackets
    		splitData = bracketSplit(teamList)
    		homeSides = splitData[0]
    		awaySides = splitData[1]

    		winningSides = []

    		i=0
    		while i < len(homeSides):
      			curWinner = runMatch(homeSides[i], awaySides[i])
      			winningSides.append(curWinner)
      			i = i + 1
      
    		teamList = winningSides

    		time.sleep(5)
    		print ''
    		print ''
    		print ''
    		print ''	

	print 'The tournament winner is ' + teamList[0]

def getRoundName(teamCount):
	#Get the string for the correct round name
	if teamCount == 64:
			roundName = 'THE ROUND OF 64'
	elif teamCount == 32:
		roundName = 'THE ROUND OF 32'
	elif teamCount == 16:
		roundName = 'THE ROUND OF 16'
	elif teamCount == 8:
		roundName = 'THE QUARTER FINALS'
	elif teamCount == 4:
		roundName = 'THE SEMI-FINALS'
	elif teamCount == 2:
		roundName = 'THE FINAL'
	else:
		roundName = 'ROUND'

	return roundName

def bracketSplit(teamList):
	#break a list of teams into 2 seperate lists at random

	#initialise random shuffle
	random.shuffle(teamList)

	#split into 2 lists
	teamCount = len(teamList)
	aTeam = teamList[0:(teamCount/2)]
	bTeam = teamList[(teamCount/2):]

	#return a list containing both lists
	return [aTeam, bTeam]
		
def runMatch(teamA, teamB):
	#gen scores for both teams
	aScore = random.randint(0,5)
	bScore = random.randint(0,5)

	#note and return winner
	if aScore > bScore:
		winTeam = teamA
	elif aScore == bScore:
		#draw
		#pick team at random and print penalty win
		penDecider = random.randint(0,1)
		if penDecider == 1:
			winTeam = teamA
			teamA = teamA + ' (p)'
		else:
			winTeam = teamB
			teamB = teamB + ' (p)'
	else:
		winTeam = teamB

	#display result
	print ''
	print teamA + ' ' + str(aScore) + ':' + str(bScore) + ' ' + teamB

	#return winning side
	return winTeam
		
#start on run 
if __name__ == '__main__':
	#List teams here as this will remain untouched
	teamGroup = teamStore.getTeamsA()

	#Give in initial random order
	random.shuffle(teamGroup)

	#Run main
	runTournament(teamGroup)

	