# src/ui/member_ui.py

import tkinter as tk
from tkinter import messagebox

from src.config import DATA_FILE_MEMBER
from src.logic.member_management import MemberManagement
from src.models.member import Member


class MemberManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Member Management System")
        self.member_management = MemberManagement(data_file=DATA_FILE_MEMBER)

        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Member Management", font=("Helvetica", 16)).pack(pady=10)

        # Member Form
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(pady=10)

        tk.Label(self.form_frame, text="Member ID:").grid(row=0, column=0, padx=5, pady=5)
        self.member_id_entry = tk.Entry(self.form_frame)
        self.member_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.form_frame)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Age:").grid(row=2, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.form_frame)
        self.age_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Health Info:").grid(row=3, column=0, padx=5, pady=5)
        self.health_info_entry = tk.Entry(self.form_frame)
        self.health_info_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Membership Status:").grid(row=4, column=0, padx=5, pady=5)
        self.membership_status_entry = tk.Entry(self.form_frame)
        self.membership_status_entry.grid(row=4, column=1, padx=5, pady=5)

        button_frame = tk.Frame(self.form_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=10)

        tk.Button(button_frame, text="Add Member", command=self.add_member).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Update Member", command=self.update_member).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remove Member", command=self.remove_member).pack(side=tk.LEFT, padx=5)

        # Members List
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(pady=10)

        self.member_listbox = tk.Listbox(self.list_frame, width=50, height=10)
        self.member_listbox.pack(side=tk.LEFT, padx=10)
        self.update_member_listbox()

        scrollbar = tk.Scrollbar(self.list_frame, orient="vertical")
        scrollbar.config(command=self.member_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.member_listbox.config(yscrollcommand=scrollbar.set)

    def add_member(self):
        member_id = self.member_id_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        health_info = self.health_info_entry.get()
        membership_status = self.membership_status_entry.get()

        if not member_id or not name or not age or not membership_status:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        member = Member(member_id, name, age, health_info, membership_status)
        self.member_management.add_member(member)
        self.update_member_listbox()
        self.clear_form()

    def update_member(self):
        selected_index = self.member_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a member to update")
            return

        member_id = self.member_id_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        health_info = self.health_info_entry.get()
        membership_status = self.membership_status_entry.get()

        if not member_id or not name or not age or not membership_status:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        selected_member = self.member_listbox.get(selected_index)
        original_member_id = selected_member.split(" - ")[0]

        member = Member(member_id, name, age, health_info, membership_status)
        self.member_management.update_member(original_member_id, member)
        self.update_member_listbox()
        self.clear_form()

    def remove_member(self):
        selected_index = self.member_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a member to remove")
            return

        selected_member = self.member_listbox.get(selected_index)
        member_id = selected_member.split(" - ")[0]

        self.member_management.remove_member(member_id)
        self.update_member_listbox()

    def update_member_listbox(self):
        self.member_listbox.delete(0, tk.END)
        for member in self.member_management.get_members():
            self.member_listbox.insert(tk.END, f"{member.member_id} - {member.name} - {member.membership_status}")

    def clear_form(self):
        self.member_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.health_info_entry.delete(0, tk.END)
        self.membership_status_entry.delete(0, tk.END)

