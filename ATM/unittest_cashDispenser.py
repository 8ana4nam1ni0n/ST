from cashDispenser import CashDispenser
import unittest

class TestCashDispenser(unittest.TestCase):

	def test_isSufficientCashAvailable_True(self):
		cd = CashDispenser()
		self.assertTrue(cd.isSufficientCashAvailable(10000))

	def test_isSufficientCashAvailable_False(self):
		cd = CashDispenser()
		self.assertFalse(cd.isSufficientCashAvailable(20000))

if __name__ == '__main__':
	unittest.main()
