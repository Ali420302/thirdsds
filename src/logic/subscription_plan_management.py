# src/logic/subscription_plan_management.py

import json
from src.models.subscription_plan import SubscriptionPlan

class SubscriptionPlanManagement:
    def __init__(self, data_file):
        self.data_file = data_file
        self.subscription_plans = self.load_subscription_plans()

    def load_subscription_plans(self):
        try:
            with open(self.data_file, 'r') as file:
                plans_data = json.load(file)
                return [SubscriptionPlan.from_dict(plan) for plan in plans_data]
        except FileNotFoundError:
            return []

    def save_subscription_plans(self):
        with open(self.data_file, 'w') as file:
            json.dump([plan.to_dict() for plan in self.subscription_plans], file, indent=4)

    def add_subscription_plan(self, plan):
        self.subscription_plans.append(plan)
        self.save_subscription_plans()

    def update_subscription_plan(self, plan_id, updated_plan):
        for i, plan in enumerate(self.subscription_plans):
            if plan.plan_id == plan_id:
                self.subscription_plans[i] = updated_plan
                self.save_subscription_plans()
                return True
        return False

    def remove_subscription_plan(self, plan_id):
        self.subscription_plans = [plan for plan in self.subscription_plans if plan.plan_id != plan_id]
        self.save_subscription_plans()

    def get_subscription_plans(self):
        return self.subscription_plans