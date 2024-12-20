# src/ui/subscription_plan_ui.py

import tkinter as tk
from tkinter import messagebox
from src.logic.subscription_plan_management import SubscriptionPlanManagement
from src.models.subscription_plan import SubscriptionPlan

from src.config import DATA_FILE_SUBSCRIPTION_PLAN


class SubscriptionPlanManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Subscription Plan Management System")
        self.plan_management = SubscriptionPlanManagement(data_file=DATA_FILE_SUBSCRIPTION_PLAN)

        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Subscription Plan Management", font=("Helvetica", 16)).pack(pady=10)

        # Plan Form
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(pady=10)

        tk.Label(self.form_frame, text="Plan ID:").grid(row=0, column=0, padx=5, pady=5)
        self.plan_id_entry = tk.Entry(self.form_frame)
        self.plan_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.form_frame)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Duration (Months):").grid(row=2, column=0, padx=5, pady=5)
        self.duration_entry = tk.Entry(self.form_frame)
        self.duration_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Rate:").grid(row=3, column=0, padx=5, pady=5)
        self.rate_entry = tk.Entry(self.form_frame)
        self.rate_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Discount:").grid(row=4, column=0, padx=5, pady=5)
        self.discount_entry = tk.Entry(self.form_frame)
        self.discount_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Promotion:").grid(row=5, column=0, padx=5, pady=5)
        self.promotion_entry = tk.Entry(self.form_frame)
        self.promotion_entry.grid(row=5, column=1, padx=5, pady=5)

        button_frame = tk.Frame(self.form_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=10)

        tk.Button(button_frame, text="Add Plan", command=self.add_plan).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Update Plan", command=self.update_plan).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remove Plan", command=self.remove_plan).pack(side=tk.LEFT, padx=5)

        # Plans List
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(pady=10)

        self.plan_listbox = tk.Listbox(self.list_frame, width=80, height=10)
        self.plan_listbox.pack(side=tk.LEFT, padx=10)
        self.update_plan_listbox()

        scrollbar = tk.Scrollbar(self.list_frame, orient="vertical")
        scrollbar.config(command=self.plan_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.plan_listbox.config(yscrollcommand=scrollbar.set)

    def add_plan(self):
        plan_id = self.plan_id_entry.get()
        name = self.name_entry.get()
        duration = self.duration_entry.get()
        rate = self.rate_entry.get()
        discount = self.discount_entry.get()
        promotion = self.promotion_entry.get()

        if not plan_id or not name or not duration or not rate:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        plan = SubscriptionPlan(plan_id, name, duration, rate, discount, promotion)
        self.plan_management.add_subscription_plan(plan)
        self.update_plan_listbox()
        self.clear_form()

    def update_plan(self):
        selected_index = self.plan_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a plan to update")
            return

        plan_id = self.plan_id_entry.get()
        name = self.name_entry.get()
        duration = self.duration_entry.get()
        rate = self.rate_entry.get()
        discount = self.discount_entry.get()
        promotion = self.promotion_entry.get()

        if not plan_id or not name or not duration or not rate:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        selected_plan = self.plan_listbox.get(selected_index)
        original_plan_id = selected_plan.split(" - ")[0]

        plan = SubscriptionPlan(plan_id, name, duration, rate, discount, promotion)
        self.plan_management.update_subscription_plan(original_plan_id, plan)
        self.update_plan_listbox()
        self.clear_form()

    def remove_plan(self):
        selected_index = self.plan_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a plan to remove")
            return

        selected_plan = self.plan_listbox.get(selected_index)
        plan_id = selected_plan.split(" - ")[0]

        self.plan_management.remove_subscription_plan(plan_id)
        self.update_plan_listbox()

    def update_plan_listbox(self):
        self.plan_listbox.delete(0, tk.END)
        for plan in self.plan_management.get_subscription_plans():
            self.plan_listbox.insert(tk.END,
                                     f"{plan.plan_id} - {plan.name} - {plan.duration_months} months - ${plan.rate} - Discount: {plan.discount}% - Promotion: {plan.promotion}")

    def clear_form(self):
        self.plan_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.rate_entry.delete(0, tk.END)
        self.discount_entry.delete(0, tk.END)
        self.promotion_entry.delete(0, tk.END)

