from transaction import Transaction

class BalanceInquiry(Transaction):
	'Represents a balance inquiry atm transaction'

	def __init__(self, accountNumber, screen, bankDatabase):
		super().__init__(accountNumber, screen, bankDatabase)

	def execute(self):
		bankDatabase = self.getBankDatabase()
		screen = self.getScreen()

		availableBalance = bankDatabase.getAvailableBalance(self.getAccountNumber())
		totalBalance = bankDatabase.getTotalBalance(self.getAccountNumber())

		screen.displayMessageLine('\nBalance Information:')
		screen.displayMessage(' - Available balance: ')
		screen.displayDollarAmount(availableBalance)
		screen.displayMessage('\n - Total Balance: ')
		screen.displayDollarAmount(totalBalance)
