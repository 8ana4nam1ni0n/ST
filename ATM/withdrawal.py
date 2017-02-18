from transaction import Transaction

class Withdrawal(Transaction):
	'Represents a withdrawal ATM transaction'

	__amount = 0
	__keypad = None
	__cashDispenser = None

	__CANCELED = 6

	def __init__(self, accountNumber, screen, bankDatabase, keypad, cashDispenser):
		super().__init__(accountNumber, screen, bankDatabase)
		self.__keypad = keypad
		self.__cashDispenser = cashDispenser

	def displayMenuOfAmounts(self):
		choice = 0
		screen = self.getScreen()
		amounts = [0, 20, 40, 60, 100, 200]

		while choice == 0:
			screen.displayMessageLine('\nWithdrawal Menu: ')
			for i in range(1, len(amounts)):
				screen.displayMessageLine(str(i) + ' - $' + str(amounts[i]))
			screen.displayMessageLine('6 - Cancel Transaction')
			# screen.displayMessage('\nChoose a withdrawal amount: ')
			input = self.__keypad.getInput('\nChoose a withdrawal amount: ')

			if 0 < input < self.__CANCELED:
				choice = amounts[input]
			elif input == self.__CANCELED:
				choice = self.__CANCELED
			else:
				screen.displayMessageLine('\nInvalid selection. Try Again.')
		return choice

	def execute(self):
		cashDispensed = False
		availableBalance = 0.0
		bankDatabase = self.getBankDatabase()
		screen = self.getScreen()
		
		while not cashDispensed:
			amount = self.displayMenuOfAmounts()
			if amount != self.__CANCELED:
				availableBalance = bankDatabase.getAvailableBalance(self.getAccountNumber())
				if amount <= availableBalance:
					if self.__cashDispenser.isSufficientCashAvailable(amount):
						bankDatabase.debit(self.getAccountNumber(), amount)
						self.__cashDispenser.dispenseCash(amount)
						cashDispensed = True
						screen.displayMessageLine('\nYour cash has been dispensed. Please take your cash now.')
					else:
						screen.displayMessageLine('\nInsufficient funds in the ATM.\n\n' \
						+ 'Please choose a smaller amount,')
				else:
					screen.displayMessageLine('\nInsufficient funds in your account.\n\n' \
					+ 'Please choose a smaller amount,')
			else:
				screen.displayMessageLine('\nCanceling Transaction...')
				return
