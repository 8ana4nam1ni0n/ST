from screen import Screen
from keypad import Keypad
from cashDispenser import CashDispenser
from depositSlot import DepositSlot
from bankDatabase import BankDatabase
from balanceInquiry import BalanceInquiry
from deposit import Deposit
from withdrawal import Withdrawal

class ATM(object):
	'Represent an Automated Teller Machine'

	__userAuthenticated = False
	__currentAccountNumber = 0
	__screen = None
	__keypad = None
	__cashDispenser = None
	__depositSlot = None
	__bankDatabase = None

	__BALANCE_INQUIRY = 1
	__WITHDRAWAL = 2
	__DEPOSIT = 3
	__EXIT = 4

	def __init__(self):
		self.__userAuthenticated = False
		self.__currentAccountNumber = 0
		self.__screen = Screen()
		self.__keypad = Keypad()
		self.__cashDispenser = CashDispenser()
		self.__depositSlot = DepositSlot()
		self.__bankDatabase = BankDatabase()

	def run(self):
		while True:
			while not self.__userAuthenticated:
				self.__screen.displayMessageLine('\nWelcome!')
				self.__authenticateUser()
			self.__performTransactions()
			self.__userAuthenticated = False
			self.__currentAccountNumber = 0
			self.__screen.displayMessageLine('\nThank you! GoodBye!')

	def __authenticateUser(self):
		# self.__screen.displayMessage('\nPlease enter your account Number: ')
		accountNumber = self.__keypad.getInput('\nPlease enter your account Number: ')
		# self.__screen.displayMessage('\nEnter your pin: ')
		pin = self.__keypad.getInput('\nEnter your pin: ')

		self.__userAuthenticated = self.__bankDatabase.authenticateUser(accountNumber, pin)
		if self.__userAuthenticated:
			self.__currentAccountNumber = accountNumber
		else:
			self.__screen.displayMessageLine('Invalid account number or pin. Please Try again.')

	def __performTransactions(self):
		transaction = None
		userExited = False

		while not userExited:
			mainMenuSelection = self.__displayMainMenu()
			if self.__BALANCE_INQUIRY <= mainMenuSelection <= self.__DEPOSIT:
				transaction = self.createTransaction(mainMenuSelection)
				transaction.execute()
			elif mainMenuSelection == self.__EXIT:
				self.__screen.displayMessageLine('\nExiting the system...')
				userExited = True
			else:
				self.__screen.displayMessageLine('\nYou did not enter a valid selection. Try again.')

	def __displayMainMenu(self):
		self.__screen.displayMessageLine('\nMain menu:')
		self.__screen.displayMessageLine('1 - View my balance')
		self.__screen.displayMessageLine('2 - Withdraw cash')
		self.__screen.displayMessageLine('3 - Deposit funds')
		self.__screen.displayMessageLine('4 - Exit\n')
		# self.__screen.displayMessage('Enter a choice: ')
		return self.__keypad.getInput('Enter a choice: ')

	def createTransaction(self, type):
		transaction = None
		if type == self.__BALANCE_INQUIRY:
			transaction = BalanceInquiry(self.__currentAccountNumber, self.__screen, self.__bankDatabase)
		elif type == self.__WITHDRAWAL:
			transaction = Withdrawal(self.__currentAccountNumber, self.__screen, self.__bankDatabase, \
				self.__keypad, self.__cashDispenser)
		else:
			transaction = Deposit(self.__currentAccountNumber, self.__screen, self.__bankDatabase, \
				self.__keypad, self.__depositSlot)
		return transaction
