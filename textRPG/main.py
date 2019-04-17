#import
import time

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
		#do option 3
		print '3'
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
	fakeLoadAnim()
	fakeLoadAnim()
	fakeLoadAnim()
	print '**Welcome ' + inventory['name'] + '**'
	fakeLoadAnim()
	main(inventory)

def statView(inventory):
	print ''
	print '~~~~~~~~~~~~~~~~~'
	print 'Stats for user: ' + str(inventory['name'])
	print 'Calls taken: ' + str(inventory['calls'])
	print 'Sales : ' + str(inventory['sales'])
	print 'Customer Satisfaction Rating: ' + str(inventory['satisfaction']) +  '%'
	print 'Breaks Taken : ' + str(inventory['breaks'])
	print '~~~~~~~~~~~~~~~~~'
	print ''

#Fake load animation to save code repetition
def fakeLoadAnim():
	print ''
	print '*'
	time.sleep(0.2)
	print '**'
	time.sleep(0.2)
	print '***'
	time.sleep(0.2)
	print '**'
	time.sleep(0.2)
	print '*'
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
		'name' : ''
	}
	#begin game
	intro(blankInv)