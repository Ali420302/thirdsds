# src/models/subscription_plan.py

class SubscriptionPlan:
    def __init__(self, plan_id, name, duration_months, rate, discount=0, promotion=None):
        self.plan_id = plan_id
        self.name = name
        self.duration_months = duration_months
        self.rate = rate
        self.discount = discount
        self.promotion = promotion

    def to_dict(self):
        return {
            "plan_id": self.plan_id,
            "name": self.name,
            "duration_months": self.duration_months,
            "rate": self.rate,
            "discount": self.discount,
            "promotion": self.promotion
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["plan_id"],
            data["name"],
            data["duration_months"],
            data["rate"],
            data.get("discount", 0),
            data.get("promotion", None)
        )