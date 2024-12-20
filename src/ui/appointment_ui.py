# src/ui/appointment_ui.py

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from src.config import DATA_FILE_APPOINTMENT
from src.logic.appointment_management import AppointmentManagement
from src.models.appointment import Appointment


class AppointmentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Appointment Management System")
        self.appointment_management = AppointmentManagement(data_file=DATA_FILE_APPOINTMENT)

        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Appointment Management", font=("Helvetica", 16)).pack(pady=10)

        # Appointment Form
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(pady=10)

        tk.Label(self.form_frame, text="Appointment ID:").grid(row=0, column=0, padx=5, pady=5)
        self.appointment_id_entry = tk.Entry(self.form_frame)
        self.appointment_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Member ID:").grid(row=1, column=0, padx=5, pady=5)
        self.member_id_entry = tk.Entry(self.form_frame)
        self.member_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Trainer ID:").grid(row=2, column=0, padx=5, pady=5)
        self.trainer_id_entry = tk.Entry(self.form_frame)
        self.trainer_id_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Appointment Type:").grid(row=3, column=0, padx=5, pady=5)
        self.appointment_type_entry = tk.Entry(self.form_frame)
        self.appointment_type_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Date & Time:").grid(row=4, column=0, padx=5, pady=5)
        self.date_time_entry = tk.Entry(self.form_frame)
        self.date_time_entry.grid(row=4, column=1, padx=5, pady=5)

        button_frame = tk.Frame(self.form_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=10)

        tk.Button(button_frame, text="Add Appointment", command=self.add_appointment).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Update Appointment", command=self.update_appointment).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remove Appointment", command=self.remove_appointment).pack(side=tk.LEFT, padx=5)

        # Appointments List
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(pady=10)

        self.appointment_listbox = tk.Listbox(self.list_frame, width=50, height=10)
        self.appointment_listbox.pack(side=tk.LEFT, padx=10)
        self.update_appointment_listbox()

        scrollbar = tk.Scrollbar(self.list_frame, orient="vertical")
        scrollbar.config(command=self.appointment_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.appointment_listbox.config(yscrollcommand=scrollbar.set)

    def add_appointment(self):
        appointment_id = self.appointment_id_entry.get()
        member_id = self.member_id_entry.get()
        trainer_id = self.trainer_id_entry.get()
        appointment_type = self.appointment_type_entry.get()
        date_time_str = self.date_time_entry.get()

        try:
            date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            messagebox.showerror("Error", "Date & Time format should be YYYY-MM-DD HH:MM:SS")
            return

        if not appointment_id or not member_id or not trainer_id or not appointment_type:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        appointment = Appointment(appointment_id, member_id, trainer_id, appointment_type, date_time)
        self.appointment_management.add_appointment(appointment)
        self.update_appointment_listbox()
        self.clear_form()

    def update_appointment(self):
        selected_index = self.appointment_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select an appointment to update")
            return

        appointment_id = self.appointment_id_entry.get()
        member_id = self.member_id_entry.get()
        trainer_id = self.trainer_id_entry.get()
        appointment_type = self.appointment_type_entry.get()
        date_time_str = self.date_time_entry.get()

        try:
            date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            messagebox.showerror("Error", "Date & Time format should be YYYY-MM-DD HH:MM:SS")
            return

        if not appointment_id or not member_id or not trainer_id or not appointment_type:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        selected_appointment = self.appointment_listbox.get(selected_index)
        original_appointment_id = selected_appointment.split(" - ")[0]

        appointment = Appointment(appointment_id, member_id, trainer_id, appointment_type, date_time)
        self.appointment_management.update_appointment(original_appointment_id, appointment)
        self.update_appointment_listbox()
        self.clear_form()

    def remove_appointment(self):
        selected_index = self.appointment_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select an appointment to remove")
            return

        selected_appointment = self.appointment_listbox.get(selected_index)
        appointment_id = selected_appointment.split(" - ")[0]

        self.appointment_management.remove_appointment(appointment_id)
        self.update_appointment_listbox()

    def update_appointment_listbox(self):
        self.appointment_listbox.delete(0, tk.END)
        for appointment in self.appointment_management.get_appointments():
            self.appointment_listbox.insert(tk.END,
                                            f"{appointment.appointment_id} - {appointment.member_id} - {appointment.appointment_type} - {appointment.date_time.strftime('%Y-%m-%d %H:%M:%S')}")

    def clear_form(self):
        self.appointment_id_entry.delete(0, tk.END)
        self.member_id_entry.delete(0, tk.END)
        self.trainer_id_entry.delete(0, tk.END)
        self.appointment_type_entry.delete(0, tk.END)
        self.date_time_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AppointmentManagementApp(root)
    root.mainloop()