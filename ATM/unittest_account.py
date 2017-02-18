from account import Account
import unittest

class TestAccount(unittest.TestCase):

	def test_isValidPin(self):
		account = Account(12345, 54321, 1000.0, 1200.0)
		self.assertTrue(account.isValidPin(54321))

	def test_isNotValidPin(self):
		account = Account(12345, 54321, 1000.0, 1200.0)
		self.assertFalse(account.isValidPin(12344))

	def test_credit_withInt(self):
		account = Account(12345, 54321, 1000.0, 1200.0)
		account.credit(200)
		self.assertEqual(account.getTotalBalance() - 200, 1200.0)

	def test_credit_withFloat(self):
		account = Account(12345, 54321, 1000.0, 1200.0)
		account.credit(200.50)
		self.assertEqual(account.getTotalBalance() - 200.50, 1200.0)

	def test_debit_withInt(self):
		account = Account(12345, 54321, 1000.0, 1200.0)
		account.debit(200)
		self.assertEqual(account.getTotalBalance() + 200, 1200.0)

	def test_debit_withFloat(self):
		account = Account(12345, 54321, 1000.0, 1200.0)
		account.debit(200.50)
		self.assertEqual(account.getTotalBalance() + 200.50, 1200.0)

if __name__ == '__main__':
	unittest.main()
