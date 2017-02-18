
class CashDispenser(object):
	'Represent the cash dispenser of an the ATM'

	__INITIAL_COUNT = 500
	__count = 0

	def __init__(self):
		self.__count = self.__INITIAL_COUNT

	def dispenseCash(self, amount):
		self.__count -= amount / 20

	def isSufficientCashAvailable(self, amount):
		billsRequired = amount / 20
		return self.__count >= billsRequired
