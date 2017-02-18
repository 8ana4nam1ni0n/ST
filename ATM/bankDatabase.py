from account import Account


class BankDatabase(object):
	'Represents the bank account database'

	__accounts = []

	def __init__(self):
		self.__accounts = []
		self.__accounts.append(Account(12345, 54321, 1000.0, 1200.0))
		self.__accounts.append(Account(98765, 56789, 200.0, 200.0))

	def getAccount(self, accountNumber):
		for account in self.__accounts:
			if account.getAccountNumber() == accountNumber:
				return account
		return None

	def authenticateUser(self, accountNumber, pin):
		isAuthenticated = False
		account = self.getAccount(accountNumber)
		if account is not None:
			isAuthenticated = account.isValidPin(pin)
		return isAuthenticated

	def getAvailableBalance(self, accountNumber):
		account = self.getAccount(accountNumber)
		return account.getAvailableBalance() if account is not None else account

	def getTotalBalance(self, accountNumber):
		account = self.getAccount(accountNumber)
		return account.getTotalBalance() if account is not None else account

	def credit(self, accountNumber, amount):
		account = self.getAccount(accountNumber)
		if account is not None:
			account.credit(amount)

	def debit(self, accountNumber, amount):
		account = self.getAccount(accountNumber)
		if account is not None:
			account.debit(amount)
