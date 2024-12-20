# src/models/payment.py

from datetime import datetime

class Payment:
    def __init__(self, payment_id, member_id, amount, payment_date, payment_method, subscription_type):
        self.payment_id = payment_id
        self.member_id = member_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_method = payment_method
        self.subscription_type = subscription_type

    def to_dict(self):
        return {
            "payment_id": self.payment_id,
            "member_id": self.member_id,
            "amount": self.amount,
            "payment_date": self.payment_date.strftime("%Y-%m-%d %H:%M:%S"),
            "payment_method": self.payment_method,
            "subscription_type": self.subscription_type
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["payment_id"],
            data["member_id"],
            data["amount"],
            datetime.strptime(data["payment_date"], "%Y-%m-%d %H:%M:%S"),
            data["payment_method"],
            data["subscription_type"]
        )