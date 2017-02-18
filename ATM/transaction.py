
class Transaction(object):
	'Represent an ATM transaction'

	__accountNumber = 0
	__screen = None
	__bankDatabase = None

	def __init__(self, accountNumber, screen, bankDatabase):
		self.__accountNumber = accountNumber
		self.__screen = screen
		self.__bankDatabase = bankDatabase

	def getAccountNumber(self):
		return self.__accountNumber

	def getScreen(self):
		return self.__screen

	def getBankDatabase(self):
		return self.__bankDatabase
