# src/logic/payment_management.py

import json
from datetime import datetime
from src.models.payment import Payment

class PaymentManagement:
    def __init__(self, data_file):
        self.data_file = data_file
        self.payments = self.load_payments()

    def load_payments(self):
        try:
            with open(self.data_file, 'r') as file:
                payments_data = json.load(file)
                return [Payment.from_dict(payment) for payment in payments_data]
        except FileNotFoundError:
            return []

    def save_payments(self):
        with open(self.data_file, 'w') as file:
            json.dump([payment.to_dict() for payment in self.payments], file, indent=4)

    def add_payment(self, payment):
        self.payments.append(payment)
        self.save_payments()

    def update_payment(self, payment_id, updated_payment):
        for i, payment in enumerate(self.payments):
            if payment.payment_id == payment_id:
                self.payments[i] = updated_payment
                self.save_payments()
                return True
        return False

    def remove_payment(self, payment_id):
        self.payments = [payment for payment in self.payments if payment.payment_id != payment_id]
        self.save_payments()

    def get_payments(self):
        return self.payments