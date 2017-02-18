from bankDatabase import BankDatabase
from account import Account
import unittest

class TestBankDatabaseIntegration(unittest.TestCase):

	def test_getAccount_when_exist(self):
		bankDB = BankDatabase()
		account1 = Account(12345, 54321, 1000.0, 1200.0)
		account2 = bankDB.getAccount(12345)
		self.assertEqual(account1, account2)

	def test_getAccount_when_not_exist(self):
		bankDB = BankDatabase()
		self.assertIsNone(bankDB.getAccount(12346))

	def test_getAccount_when_is_not_none(self):
		bankDB = BankDatabase()
		self.assertIsNotNone(bankDB.getAccount(12345))

	def test_autheticateUser_valid(self):
		bankDB = BankDatabase()
		self.assertTrue(bankDB.authenticateUser(12345, 54321))

	def test_autheticateUser_not_valid(self):
		bankDB = BankDatabase()
		self.assertFalse(bankDB.authenticateUser(12345, 12345))

	def test_credit_account_exist(self):
		bankDB = BankDatabase()
		bankDB.credit(12345, 200)
		self.assertEqual(bankDB.getTotalBalance(12345) - 200, 1200)

	def test_credit_account_not_exist(self):
		bankDB = BankDatabase()
		bankDB.credit(123456, 200)
		self.assertEqual(bankDB.getTotalBalance(12345), 1200)

	def test_debit_account_exist(self):
		bankDB = BankDatabase()
		bankDB.debit(12345, 200)
		self.assertEqual(bankDB.getTotalBalance(12345) + 200, 1200)

	def test_debit_account_not_exist(self):
		bankDB = BankDatabase()
		bankDB.debit(123456, 200)
		self.assertEqual(bankDB.getTotalBalance(12345), 1200)

	def test_getTotalBalance_when_exist(self):
		bankDB = BankDatabase()
		self.assertEqual(bankDB.getTotalBalance(98765), 200)

	def test_getTotalBalance_when_exist(self):
		bankDB = BankDatabase()
		self.assertIsNone(bankDB.getTotalBalance(987654))

	def test_getAvailableBalance_when_exist(self):
		bankDB = BankDatabase()
		self.assertEqual(bankDB.getAvailableBalance(98765), 200)

	def test_getAvailableBalance_when_exist(self):
		bankDB = BankDatabase()
		self.assertIsNone(bankDB.getAvailableBalance(987654))

if __name__ == '__main__':
	unittest.main()
