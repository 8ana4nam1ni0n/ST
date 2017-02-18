from atm import ATM
from balanceInquiry import BalanceInquiry
from deposit import Deposit
from withdrawal import Withdrawal
import unittest

class TestATMIntegration(unittest.TestCase):

	def test_createTransaction_when_balanaceInquiry(self):
		balanceInquiry = 1
		atm = ATM()
		self.assertIsInstance(atm.createTransaction(balanceInquiry), BalanceInquiry)

	def test_createTransaction_when_withdrawal(self):
			withdrawal = 2
			atm = ATM()
			self.assertIsInstance(atm.createTransaction(withdrawal), Withdrawal)

	def test_createTransaction_when_Deposit(self):
		deposit = 3
		atm = ATM()
		self.assertIsInstance(atm.createTransaction(deposit), Deposit)

	def test_createTransaction_when_None(self):
		invalid = 4
		atm = ATM()
		self.assertIsNone(atm.createTransaction(invalid))


if __name__ == '__main__':
	unittest.main()
