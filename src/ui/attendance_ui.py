# src/ui/attendance_ui.py

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from src.config import DATA_FILE_ATTENDANCE
from src.logic.attendance_management import AttendanceManagement
from src.models.attendance import Attendance


class AttendanceManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")
        self.attendance_management = AttendanceManagement(data_file=DATA_FILE_ATTENDANCE)

        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Attendance Management", font=("Helvetica", 16)).pack(pady=10)

        # Attendance Form
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(pady=10)

        tk.Label(self.form_frame, text="Attendance ID:").grid(row=0, column=0, padx=5, pady=5)
        self.attendance_id_entry = tk.Entry(self.form_frame)
        self.attendance_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Member ID:").grid(row=1, column=0, padx=5, pady=5)
        self.member_id_entry = tk.Entry(self.form_frame)
        self.member_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Class ID:").grid(row=2, column=0, padx=5, pady=5)
        self.class_id_entry = tk.Entry(self.form_frame)
        self.class_id_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Check-in Time:").grid(row=3, column=0, padx=5, pady=5)
        self.check_in_time_entry = tk.Entry(self.form_frame)
        self.check_in_time_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Check-out Time:").grid(row=4, column=0, padx=5, pady=5)
        self.check_out_time_entry = tk.Entry(self.form_frame)
        self.check_out_time_entry.grid(row=4, column=1, padx=5, pady=5)

        button_frame = tk.Frame(self.form_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=10)

        tk.Button(button_frame, text="Add Attendance", command=self.add_attendance).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Update Attendance", command=self.update_attendance).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remove Attendance", command=self.remove_attendance).pack(side=tk.LEFT, padx=5)

        # Attendance List
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(pady=10)

        self.attendance_listbox = tk.Listbox(self.list_frame, width=80, height=10)
        self.attendance_listbox.pack(side=tk.LEFT, padx=10)
        self.update_attendance_listbox()

        scrollbar = tk.Scrollbar(self.list_frame, orient="vertical")
        scrollbar.config(command=self.attendance_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.attendance_listbox.config(yscrollcommand=scrollbar.set)

        # Reports Frame
        self.report_frame = tk.Frame(self.root)
        self.report_frame.pack(pady=10)

        tk.Button(self.report_frame, text="Member Attendance Report", command=self.member_attendance_report).pack(
            side=tk.LEFT, padx=5)
        tk.Button(self.report_frame, text="Class Popularity Report", command=self.class_popularity_report).pack(
            side=tk.LEFT, padx=5)
        tk.Button(self.report_frame, text="Peak Hours Report", command=self.peak_hours_report).pack(side=tk.LEFT,
                                                                                                    padx=5)

    def add_attendance(self):
        attendance_id = self.attendance_id_entry.get()
        member_id = self.member_id_entry.get()
        class_id = self.class_id_entry.get()
        check_in_time_str = self.check_in_time_entry.get()
        check_out_time_str = self.check_out_time_entry.get()

        try:
            check_in_time = datetime.strptime(check_in_time_str, "%Y-%m-%d %H:%M:%S")
            check_out_time = datetime.strptime(check_out_time_str, "%Y-%m-%d %H:%M:%S") if check_out_time_str else None
        except ValueError:
            messagebox.showerror("Error", "Date format should be YYYY-MM-DD HH:MM:SS")
            return

        if not attendance_id or not member_id or not class_id or not check_in_time_str:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        attendance = Attendance(attendance_id, member_id, class_id, check_in_time, check_out_time)
        self.attendance_management.add_attendance(attendance)
        self.update_attendance_listbox()
        self.clear_form()

    def update_attendance(self):
        selected_index = self.attendance_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select an attendance record to update")
            return

        attendance_id = self.attendance_id_entry.get()
        member_id = self.member_id_entry.get()
        class_id = self.class_id_entry.get()
        check_in_time_str = self.check_in_time_entry.get()
        check_out_time_str = self.check_out_time_entry.get()

        try:
            check_in_time = datetime.strptime(check_in_time_str, "%Y-%m-%d %H:%M:%S")
            check_out_time = datetime.strptime(check_out_time_str, "%Y-%m-%d %H:%M:%S") if check_out_time_str else None
        except ValueError:
            messagebox.showerror("Error", "Date format should be YYYY-MM-DD HH:MM:SS")
            return

        if not attendance_id or not member_id or not class_id or not check_in_time_str:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        selected_attendance = self.attendance_listbox.get(selected_index)
        original_attendance_id = selected_attendance.split(" - ")[0]

        attendance = Attendance(attendance_id, member_id, class_id, check_in_time, check_out_time)
        self.attendance_management.update_attendance(original_attendance_id, attendance)
        self.update_attendance_listbox()
        self.clear_form()

    def remove_attendance(self):
        selected_index = self.attendance_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select an attendance record to remove")
            return

        selected_attendance = self.attendance_listbox.get(selected_index)
        attendance_id = selected_attendance.split(" - ")[0]

        self.attendance_management.remove_attendance(attendance_id)
        self.update_attendance_listbox()

    def update_attendance_listbox(self):
        self.attendance_listbox.delete(0, tk.END)
        for attendance in self.attendance_management.get_attendances():
            self.attendance_listbox.insert(tk.END,
                                           f"{attendance.attendance_id} - {attendance.member_id} - {attendance.class_id} - {attendance.check_in_time.strftime('%Y-%m-%d %H:%M:%S')} - {attendance.check_out_time.strftime('%Y-%m-%d %H:%M:%S') if attendance.check_out_time else 'N/A'}")

    def clear_form(self):
        self.attendance_id_entry.delete(0, tk.END)
        self.member_id_entry.delete(0, tk.END)
        self.class_id_entry.delete(0, tk.END)
        self.check_in_time_entry.delete(0, tk.END)
        self.check_out_time_entry.delete(0, tk.END)

    def member_attendance_report(self):
        member_id = self.member_id_entry.get()
        if not member_id:
            messagebox.showerror("Error", "Please enter a member ID")
            return

        attendances = self.attendance_management.get_attendance_by_member(member_id)
        report = f"Attendance Report for Member ID: {member_id}\n\n"
        for attendance in attendances:
            report += f"Class ID: {attendance.class_id}, Check-in: {attendance.check_in_time}, Check-out: {attendance.check_out_time if attendance.check_out_time else 'N/A'}\n"
        messagebox.showinfo("Member Attendance Report", report)

    def class_popularity_report(self):
        class_id = self.class_id_entry.get()
        if not class_id:
            messagebox.showerror("Error", "Please enter a class ID")
            return

        attendances = self.attendance_management.get_attendance_by_class(class_id)
        report = f"Class Popularity Report for Class ID: {class_id}\n\n"
        for attendance in attendances:
            report += f"Member ID: {attendance.member_id}, Check-in: {attendance.check_in_time}, Check-out: {attendance.check_out_time if attendance.check_out_time else 'N/A'}\n"
        messagebox.showinfo("Class Popularity Report", report)

    def peak_hours_report(self):
        peak_hours = self.attendance_management.get_peak_hours()
        report = "Peak Hours Report\n\n"
        for hour, count in enumerate(peak_hours):
            report += f"{hour:02d}:00 - {count} check-ins\n"
        messagebox.showinfo("Peak Hours Report", report)

