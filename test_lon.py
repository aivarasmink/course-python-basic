import unittest
from lon_calculiator import calculate_monthly_payment

class TestCalculateMonthlyPayment(unittest.TestCase):

    def test_normal(self):
        loan_amount = 10000
        interest_rate = 5
        loan_term = 5
        expected = 212.47
        self.assertAlmostEqual(calculate_monthly_payment(loan_amount, interest_rate, loan_term), expected, delta=0.01)
    
    def test_zero_interest(self):
        loan_amount = 10000
        interest_rate = 0
        loan_term = 5
        expected = 166.67
        self.assertAlmostEqual(calculate_monthly_payment(loan_amount, interest_rate, loan_term), expected, delta=0.01)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculate_monthly_payment('invalid', 5, 5)
        
        with self.assertRaises(ValueError):
            calculate_monthly_payment(10000, 'invalid', 5)

        with self.assertRaises(ValueError):
            calculate_monthly_payment(10000, 5, 'invalid')

    def test_large_loan(self):
        loan_amount = 10000000000
        interest_rate = 10
        loan_term = 30
        expected = 954166.67
        self.assertAlmostEqual(calculate_monthly_payment(loan_amount, interest_rate, loan_term), expected, delta=1000)

if __name__ == "__main__":
    unittest.main()
