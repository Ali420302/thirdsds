# src/ui/payment_ui.py

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from src.config import DATA_FILE_PAYMENT
from src.logic.payment_management import PaymentManagement
from src.models.payment import Payment


class PaymentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Payment Management System")
        self.payment_management = PaymentManagement(data_file=DATA_FILE_PAYMENT)

        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Payment Management", font=("Helvetica", 16)).pack(pady=10)

        # Payment Form
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(pady=10)

        tk.Label(self.form_frame, text="Payment ID:").grid(row=0, column=0, padx=5, pady=5)
        self.payment_id_entry = tk.Entry(self.form_frame)
        self.payment_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Member ID:").grid(row=1, column=0, padx=5, pady=5)
        self.member_id_entry = tk.Entry(self.form_frame)
        self.member_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Amount:").grid(row=2, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(self.form_frame)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Payment Date:").grid(row=3, column=0, padx=5, pady=5)
        self.payment_date_entry = tk.Entry(self.form_frame)
        self.payment_date_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Payment Method:").grid(row=4, column=0, padx=5, pady=5)
        self.payment_method_entry = tk.Entry(self.form_frame)
        self.payment_method_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Subscription Type:").grid(row=5, column=0, padx=5, pady=5)
        self.subscription_type_entry = tk.Entry(self.form_frame)
        self.subscription_type_entry.grid(row=5, column=1, padx=5, pady=5)

        button_frame = tk.Frame(self.form_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=10)

        tk.Button(button_frame, text="Add Payment", command=self.add_payment).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Update Payment", command=self.update_payment).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remove Payment", command=self.remove_payment).pack(side=tk.LEFT, padx=5)

        # Payments List
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(pady=10)

        self.payment_listbox = tk.Listbox(self.list_frame, width=50, height=10)
        self.payment_listbox.pack(side=tk.LEFT, padx=10)
        self.update_payment_listbox()

        scrollbar = tk.Scrollbar(self.list_frame, orient="vertical")
        scrollbar.config(command=self.payment_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.payment_listbox.config(yscrollcommand=scrollbar.set)

    def add_payment(self):
        payment_id = self.payment_id_entry.get()
        member_id = self.member_id_entry.get()
        amount = self.amount_entry.get()
        payment_date_str = self.payment_date_entry.get()
        payment_method = self.payment_method_entry.get()
        subscription_type = self.subscription_type_entry.get()

        try:
            payment_date = datetime.strptime(payment_date_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            messagebox.showerror("Error", "Payment Date format should be YYYY-MM-DD HH:MM:SS")
            return

        if not payment_id or not member_id or not amount or not payment_method or not subscription_type:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        payment = Payment(payment_id, member_id, amount, payment_date, payment_method, subscription_type)
        self.payment_management.add_payment(payment)
        self.update_payment_listbox()
        self.clear_form()

    def update_payment(self):
        selected_index = self.payment_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a payment to update")
            return

        payment_id = self.payment_id_entry.get()
        member_id = self.member_id_entry.get()
        amount = self.amount_entry.get()
        payment_date_str = self.payment_date_entry.get()
        payment_method = self.payment_method_entry.get()
        subscription_type = self.subscription_type_entry.get()

        try:
            payment_date = datetime.strptime(payment_date_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            messagebox.showerror("Error", "Payment Date format should be YYYY-MM-DD HH:MM:SS")
            return

        if not payment_id or not member_id or not amount or not payment_method or not subscription_type:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        selected_payment = self.payment_listbox.get(selected_index)
        original_payment_id = selected_payment.split(" - ")[0]

        payment = Payment(payment_id, member_id, amount, payment_date, payment_method, subscription_type)
        self.payment_management.update_payment(original_payment_id, payment)
        self.update_payment_listbox()
        self.clear_form()

    def remove_payment(self):
        selected_index = self.payment_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a payment to remove")
            return

        selected_payment = self.payment_listbox.get(selected_index)
        payment_id = selected_payment.split(" - ")[0]

        self.payment_management.remove_payment(payment_id)
        self.update_payment_listbox()

    def update_payment_listbox(self):
        self.payment_listbox.delete(0, tk.END)
        for payment in self.payment_management.get_payments():
            self.payment_listbox.insert(tk.END,
                                        f"{payment.payment_id} - {payment.member_id} - {payment.amount} - {payment.payment_date.strftime('%Y-%m-%d %H:%M:%S')}")

    def clear_form(self):
        self.payment_id_entry.delete(0, tk.END)
        self.member_id_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.payment_date_entry.delete(0, tk.END)
        self.payment_method_entry.delete(0, tk.END)
        self.subscription_type_entry.delete(0, tk.END)
