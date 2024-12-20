# tests/test_payment_management.py

import unittest
import json
import os
from datetime import datetime
from src.models.payment import Payment
from src.logic.payment_management import PaymentManagement

class TestPaymentManagement(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_payments.json'
        self.sample_data = [
            {
                "payment_id": "1",
                "member_id": "1",
                "amount": "12",
                "payment_date": "2001-11-11 11:11:11",
                "payment_method": "card",
                "subscription_type": "premium"
            }
        ]
        with open(self.test_file, 'w') as file:
            json.dump(self.sample_data, file, indent=4)

        self.payment_management = PaymentManagement(self.test_file)

    def tearDown(self):
        os.remove(self.test_file)

    def test_load_payments(self):
        payments = self.payment_management.get_payments()
        self.assertEqual(len(payments), 1)
        self.assertEqual(payments[0].payment_id, "1")

    def test_add_payment(self):
        new_payment = Payment(
            payment_id="2",
            member_id="2",
            amount="20",
            payment_date=datetime.strptime("2002-12-12 12:12:12", "%Y-%m-%d %H:%M:%S"),
            payment_method="cash",
            subscription_type="basic"
        )
        self.payment_management.add_payment(new_payment)
        payments = self.payment_management.get_payments()
        self.assertEqual(len(payments), 2)
        self.assertEqual(payments[1].payment_id, "2")

    def test_update_payment(self):
        updated_payment = Payment(
            payment_id="1",
            member_id="1",
            amount="15",
            payment_date=datetime.strptime("2001-11-11 11:11:11", "%Y-%m-%d %H:%M:%S"),
            payment_method="card",
            subscription_type="premium"
        )
        result = self.payment_management.update_payment("1", updated_payment)
        self.assertTrue(result)
        payments = self.payment_management.get_payments()
        self.assertEqual(payments[0].amount, "15")

    def test_remove_payment(self):
        self.payment_management.remove_payment("1")
        payments = self.payment_management.get_payments()
        self.assertEqual(len(payments), 0)

    def test_get_payments(self):
        payments = self.payment_management.get_payments()
        self.assertEqual(len(payments), 1)
        self.assertEqual(payments[0].payment_id, "1")

if __name__ == '__main__':
    unittest.main()