
class Account(object):
	'Represents a Bank Account'

	__accountNumber = 0
	__pin = 0
	__availableBalance = 0.0
	__totalBalance = 0.0

	def __init__(self, accountNumber, pin, availableBalance, totalBalance):
		self.__accountNumber = accountNumber
		self.__pin = pin
		self.__availableBalance = availableBalance
		self.__totalBalance = totalBalance

	def __eq__(self, otherAccount):
		return self.__accountNumber == otherAccount.getAccountNumber()

	def isValidPin(self, pin):
		return self.__pin == pin

	def getAvailableBalance(self):
		return self.__availableBalance

	def getTotalBalance(self):
		return self.__totalBalance

	def getAccountNumber(self):
		return self.__accountNumber

	def credit(self, amount):
		self.__totalBalance += amount

	def debit(self, amount):
		self.__availableBalance -= amount
		self.__totalBalance -= amount
