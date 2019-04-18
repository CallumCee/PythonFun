#import
import time
import random

def main(inventory):
	phoneMenu()
	#Prompt user for input and error handle input to ensure format compliance
	errorStricken = True
	while errorStricken:
		#users selection
		userSelect = raw_input()

		#catch any initial non-int inputs
		try:
			selectionInt = int(userSelect)
		except:
			print ''
			print '**invalid input**'
			print ''
			phoneMenu()
			continue

		#catch any int outside selection value range
		if selectionInt < 1 or selectionInt > 5:
			print ''
			print '**invalid input**'
			print ''
			phoneMenu()
			continue

		#if reached then reasonably tested for input compliance
		errorStricken = False

	#User selection now case by case
	if selectionInt == 1:
		#do option 1
		print '1'
	elif selectionInt ==2:
		#stat view
		fakeLoadAnim()
		statView(inventory)
	elif selectionInt ==3:
		#browse web
		fakeLoadAnim()
		webBrowse(inventory)
	elif selectionInt ==4:
		#do option 4
		print '4'
	elif selectionInt ==5:
		#do option 5
		print '5'
	else:
		print 'excuse me?'

#the intro sequence that sets up the context for the player
def intro(inventory):
	#TODO: add intro scene setting before boot sequence (story beginning)
	#animated boot sequence to main menu for introduction
	print '**Booting device**'
	fakeLoadAnim()
	print '**Sitrox Beta 3.0.2**'
	fakeLoadAnim()
	print '**Please enter your username**'
	inventory['name'] = raw_input()
	fakeLoadAnim()
	print '**logging in**'
	time.sleep(1)
	fakeLoadAnim()
	print '**Welcome ' + inventory['name'] + '**'
	time.sleep(2)
	fakeLoadAnim()
	main(inventory)

#Menu option to display stats
def statView(inventory):
	print ''
	print '~~~~~~~~~~~~~~~~~'
	print 'Stats for user: ' + str(inventory['name'])
	print 'Calls taken: ' + str(inventory['calls'])
	print 'Sales: ' + str(inventory['sales'])
	print 'Customer Satisfaction Rating: ' + str(inventory['satisfaction'])
  	print 'Manager Approval Rating: ' + str(inventory['approval'])
	print 'Breaks Taken: ' + str(inventory['breaks'])
  	print 'Morale: ' + str(inventory['morale'])
	print '~~~~~~~~~~~~~~~~~'
	print ''
	
	#exit back to main menu
	time.sleep(3)
	fakeLoadAnim()
	main(inventory)

#Menu option to browse web
def webBrowse(inventory):
  #random scenarios that give pos/neg to morale stat
  #give a random chance to give pos/neg to manager approval stat
  #scenarios presented as arrays with [info, morale, approval]

	#initialise scenario list
	scenarioStore = [
		['[Blah blah blah]',10,0],
		['[Dah Dah Dah]',0,-30],
		['[Cah Cah Cah]',10,-10]
	]

	#begin display for user
	print '[You open the browser to begin surfing the web]'
	time.sleep(2)
	fakeLoadAnim()

	#randomly select scenario and apply the stats effect
	curScenario = random.choice(scenarioStore)

	#split curScenario into print statements from each array element
	print curScenario[0]
	print ''
	print '~~~~~~~~~~~~~~~~~'
	print 'Morale: ' + str(curScenario[1])
	print 'Manager Approval: ' + str(curScenario[2])
	print '~~~~~~~~~~~~~~~~~'
	print ''

	#increment/reduce the actual stat values
	inventory['morale'] = inventory['morale'] + curScenario[1]
	inventory['approval'] = inventory['approval'] + curScenario[2]
		
	#exit back to main menu
	time.sleep(7)
	fakeLoadAnim()
	main(inventory)
	
#Fake load animation to save code repetition
def fakeLoadAnim():
	print ''
	print '~'
	time.sleep(0.2)
	print '~~'
	time.sleep(0.2)
	print '~~~'
	time.sleep(0.2)
	print '~~~~'
	time.sleep(0.2)
	print '~~~~~'
	time.sleep(0.2)
	print ''

def phoneMenu():
	print ''
	print '~~~~~~~~~~~~~~~~~'
	print '(1) Take Call'
	print '(2) View Stats'
	print '(3) Browse Web'
	print '(4) Take Break'
	print '(5) Log Off'
	print '~~~~~~~~~~~~~~~~~'
	print ''

#start on run
if __name__ == '__main__':
	#initiate the inventory
	blankInv = {
		'calls' : 0,
		'breaks' : 0,
		'sales' : 0,
		'satisfaction' : 50,
		'name' : '',
			'morale' : 50,
			'approval' : 50
	}
	#begin game
	intro(blankInv)
