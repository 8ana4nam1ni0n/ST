from transaction import Transaction

class Deposit(Transaction):
	'Represents a deposit ATM transaction'

	__amount = 0.0
	__keypad = None
	__depositSlot = None

	__CANCELED = 0

	def __init__(self, accountNumber, screen, bankDatabase, keypad, depositSlot):
		super().__init__(accountNumber, screen, bankDatabase)
		self.__keypad = keypad
		self.__depositSlot = depositSlot

	def __promptForDepositAmount(self):
		screen = self.getScreen()
		# screen.displayMessage('\nPlease Enter Deposit amount in cents or 0 to cancel: ')
		input = self.__keypad.getInput('\nPlease Enter Deposit amount in cents or 0 to cancel: ')

		if input == self.__CANCELED:
			return self.__CANCELED
		else:
			return input / 100

	def execute(self):
		bankDatabase = self.getBankDatabase()
		screen = self.getScreen()
		amount = self.__promptForDepositAmount()

		if amount != self.__CANCELED:
			screen.displayMessage('\nPlease insert a deposit envelope containing ' )
			screen.displayDollarAmount(amount)
			screen.displayMessageLine('.')

			envelopeReceived = self.__depositSlot.isEnvelopeReceived()

			if envelopeReceived:
				screen.displayMessageLine('\nYour envelope has been ' \
				+ 'received. \nNote: The money just deposited will not ' \
				+ 'be available until we verify the amount of any ' \
				+ 'enclosed cash and your checks clear.')
				bankDatabase.credit(self.getAccountNumber(), amount)
			else:
				screen.displayMessage('\nYou did not inserted an envelope, ' \
				+ 'so the ATM canceled your transaction.' )
		else:
			screen.displayMessageLine('\nCanceling Transaction...')
