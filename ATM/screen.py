
class Screen(object):
	'Represents the screen of an ATM'

	def displayMessage(self, msg):
		print(msg, end='')

	def displayMessageLine(self, msg):
		print(msg)

	def displayDollarAmount(self, amount):
		print('$' + format(amount, ',.2f'))
	
