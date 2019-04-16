#import
import time

def main(inventory):
	print ''
	print '~~~~~~~~~~~~~~~~~'
	print '(1) Take Call'
	print '(2) View Stats'
	print '(3) Browse Web'
	print '(4) Take Break'
	print '(5) Log Off'
	print '~~~~~~~~~~~~~~~~~'
	print ''

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
			continue

		#catch any int outside selection value range
		if selectionInt < 1 or selectionInt > 5:
			print ''
			print '**invalid input**'
			print ''
			continue

		#if reached then reasonably tested for input compliance
		errorStricken = False

	#User selection now case by case
	if selectionInt == 1:
		#do option 1
	elif selectionInt ==2:
		#do option 2
	elif selectionInt ==3:
		#do option 3
	elif selectionInt ==4:
		#do option 4
	elif selectionInt ==5:
		#do option 5
	else:
		break



#the intro sequence that sets up the context for the player
def intro(inventory):
	#TODO: add intro scene setting before boot sequence (story beginning)
	#animated boot sequence to main menu for introduction
	print 'Booting device'
	time.sleep(1)
	print ''
	print '...'
	print ''
	time.sleep(1)
	print 'Sitrox Beta 3.0.2'
	time.sleep(1)
	print ''
	print '...'
	print ''
	time.sleep(1)
	print 'Please enter your username'
	inventory['name'] = raw_input()
	time.sleep(1)
	print ''
	print '...'
	print ''
	time.sleep(1)
	print 'logging in'
	time.sleep(1)
	print ''
	print '...'
	print ''
	time.sleep(1)
	print ''
	print '...'
	print ''
	time.sleep(1)
	print '**Welcome ' + inventory['name'] + '**'
	time.sleep(1)
	print ''
	print '...'
	print ''
	time.sleep(1)
	print ''
	print '...'
	print ''
	time.sleep(1)
	print ''
	print '...'
	print ''
	time.sleep(2)
	main(inventory)

#start on run
if __name__ == '__main__':
	blankInv = {}
	intro(blankInv)