# src/ui/dashboard_ui.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from src.config import DATA_FILE_MEMBERSHIP_GROWTH, DATA_FILE_REVENUE_TRENDS, DATA_FILE_TRAINER_SCHEDULES, \
    DATA_FILE_EQUIPMENT_MAINTENANCE
from src.logic.staff_manager import StaffManager
from src.models.membership_growth import MembershipGrowth
from src.models.revenue_trends import RevenueTrends
from src.models.trainer_schedules import TrainerSchedule
from src.models.equipment_maintenance import EquipmentMaintenance
from datetime import datetime

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Staff Management Dashboard")

        self.staff_manager = StaffManager(
            membership_file=DATA_FILE_MEMBERSHIP_GROWTH,
            revenue_file=DATA_FILE_REVENUE_TRENDS,
            schedules_file=DATA_FILE_TRAINER_SCHEDULES,
            maintenance_file=DATA_FILE_EQUIPMENT_MAINTENANCE
        )

        self.create_widgets()

    def create_widgets(self):
        # Create Notebook (Tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

        # Membership Growth Tab
        self.membership_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.membership_frame, text="Membership Growth")
        self.create_membership_tab()

        # Revenue Trends Tab
        self.revenue_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.revenue_frame, text="Revenue Trends")
        self.create_revenue_tab()

        # Trainer Schedules Tab
        self.schedules_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.schedules_frame, text="Trainer Schedules")
        self.create_schedules_tab()

        # Equipment Maintenance Tab
        self.maintenance_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.maintenance_frame, text="Equipment Maintenance")
        self.create_maintenance_tab()

        self.create_buttons()

    def create_membership_tab(self):
        self.membership_tree = ttk.Treeview(self.membership_frame, columns=('ID', 'Date', 'New Members', 'Total Members'), show='headings')
        self.membership_tree.heading('ID', text='ID')
        self.membership_tree.heading('Date', text='Date')
        self.membership_tree.heading('New Members', text='New Members')
        self.membership_tree.heading('Total Members', text='Total Members')
        self.membership_tree.pack(expand=True, fill='both')

        self.load_membership_data()

        self.membership_form = ttk.Frame(self.membership_frame)
        self.membership_form.pack(fill='x', pady=10)

        ttk.Label(self.membership_form, text="ID:").pack(side=tk.LEFT, padx=5)
        self.membership_id_entry = ttk.Entry(self.membership_form)
        self.membership_id_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(self.membership_form, text="Date (YYYY-MM-DD):").pack(side=tk.LEFT, padx=5)
        self.membership_date_entry = ttk.Entry(self.membership_form)
        self.membership_date_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(self.membership_form, text="New Members:").pack(side=tk.LEFT, padx=5)
        self.membership_new_members_entry = ttk.Entry(self.membership_form)
        self.membership_new_members_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(self.membership_form, text="Total Members:").pack(side=tk.LEFT, padx=5)
        self.membership_total_members_entry = ttk.Entry(self.membership_form)
        self.membership_total_members_entry.pack(side=tk.LEFT, padx=5)

    def load_membership_data(self):
        self.membership_tree.delete(*self.membership_tree.get_children())
        for record in self.staff_manager.membership_records:
            self.membership_tree.insert('', tk.END, values=(record.id, record.date.strftime('%Y-%m-%d'), record.new_members, record.total_members))

    def create_revenue_tab(self):
        self.revenue_tree = ttk.Treeview(self.revenue_frame, columns=('ID', 'Date', 'Revenue'), show='headings')
        self.revenue_tree.heading('ID', text='ID')
        self.revenue_tree.heading('Date', text='Date')
        self.revenue_tree.heading('Revenue', text='Revenue')
        self.revenue_tree.pack(expand=True, fill='both')

        self.load_revenue_data()

        self.revenue_form = ttk.Frame(self.revenue_frame)
        self.revenue_form.pack(fill='x', pady=10)

        ttk.Label(self.revenue_form, text="ID:").pack(side=tk.LEFT, padx=5)
        self.revenue_id_entry = ttk.Entry(self.revenue_form)
        self.revenue_id_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(self.revenue_form, text="Date (YYYY-MM-DD):").pack(side=tk.LEFT, padx=5)
        self.revenue_date_entry = ttk.Entry(self.revenue_form)
        self.revenue_date_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(self.revenue_form, text="Revenue:").pack(side=tk.LEFT, padx=5)
        self.revenue_revenue_entry = ttk.Entry(self.revenue_form)
        self.revenue_revenue_entry.pack(side=tk.LEFT, padx=5)

    def load_revenue_data(self):
        self.revenue_tree.delete(*self.revenue_tree.get_children())
        for record in self.staff_manager.revenue_records:
            self.revenue_tree.insert('', tk.END, values=(record.id, record.date.strftime('%Y-%m-%d'), record.revenue))

    def create_schedules_tab(self):
        self.schedules_tree = ttk.Treeview(self.schedules_frame, columns=('ID', 'Trainer ID', 'Trainer Name', 'Class Name', 'Start Time', 'End Time'), show='headings')
        self.schedules_tree.heading('ID', text='ID')
        self.schedules_tree.heading('Trainer ID', text='Trainer ID')
        self.schedules_tree.heading('Trainer Name', text='Trainer Name')
        self.schedules_tree.heading('Class Name', text='Class Name')
        self.schedules_tree.heading('Start Time', text='Start Time')
        self.schedules_tree.heading('End Time', text='End Time')
        self.schedules_tree.pack(expand=True, fill='both')

        self.load_schedules_data()

        self.schedules_form = ttk.Frame(self.schedules_frame)
        self.schedules_form.pack(fill='x', pady=10)

        ttk.Label(self.schedules_form, text="ID:").pack(side=tk.LEFT, padx=5)
        self.schedules_id_entry = ttk.Entry(self.schedules_form)
        self.schedules_id_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(self.schedules_form, text="Trainer ID:").pack(side=tk.LEFT, padx=5)
        self.schedules_trainer_id_entry = ttk.Entry(self.schedules_form)
        self.schedules_trainer_id_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(self.schedules_form, text="Trainer Name:").pack(side=tk.LEFT, padx=5)
        self.schedules_trainer_name_entry = ttk.Entry(self.schedules_form)
        self.schedules_trainer_name_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(self.schedules_form, text="Class Name:").pack(side=tk.LEFT, padx=5)
        self.schedules_class_name_entry = ttk.Entry(self.schedules_form)
        self.schedules_class_name_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(self.schedules_form, text="Start Time (HH:MM:SS):").pack(side=tk.LEFT, padx=5)
        self.schedules_start_time_entry = ttk.Entry(self.schedules_form)
        self.schedules_start_time_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(self.schedules_form, text="End Time (HH:MM:SS):").pack(side=tk.LEFT, padx=5)
        self.schedules_end_time_entry = ttk.Entry(self.schedules_form)
        self.schedules_end_time_entry.pack(side=tk.LEFT, padx=5)

    def load_schedules_data(self):
        self.schedules_tree.delete(*self.schedules_tree.get_children())
        for record in self.staff_manager.schedules_records:
            self.schedules_tree.insert('', tk.END, values=(record.id, record.trainer_id, record.trainer_name, record.class_name, record.start_time.strftime('%H:%M:%S'), record.end_time.strftime('%H:%M:%S')))

    def create_maintenance_tab(self):
        self.maintenance_tree = ttk.Treeview(self.maintenance_frame, columns=('ID', 'Equipment Name', 'Last Maintenance', 'Next Maintenance', 'Status'), show='headings')
        self.maintenance_tree.heading('ID', text='ID')
        self.maintenance_tree.heading('Equipment Name', text='Equipment Name')
        self.maintenance_tree.heading('Last Maintenance', text='Last Maintenance')
        self.maintenance_tree.heading('Next Maintenance', text='Next Maintenance')
        self.maintenance_tree.heading('Status', text='Status')
        self.maintenance_tree.pack(expand=True, fill='both')

        self.load_maintenance_data()

        self.maintenance_form = ttk.Frame(self.maintenance_frame)
        self.maintenance_form.pack(fill='x', pady=10)

        ttk.Label(self.maintenance_form, text="ID:").pack(side=tk.LEFT, padx=5)
        self.maintenance_id_entry = ttk.Entry(self.maintenance_form)
        self.maintenance_id_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(self.maintenance_form, text="Equipment Name:").pack(side=tk.LEFT, padx=5)
        self.maintenance_equipment_name_entry = ttk.Entry(self.maintenance_form)
        self.maintenance_equipment_name_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(self.maintenance_form, text="Last Maintenance (YYYY-MM-DD):").pack(side=tk.LEFT, padx=5)
        self.maintenance_last_maintenance_entry = ttk.Entry(self.maintenance_form)
        self.maintenance_last_maintenance_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(self.maintenance_form, text="Next Maintenance (YYYY-MM-DD):").pack(side=tk.LEFT, padx=5)
        self.maintenance_next_maintenance_entry = ttk.Entry(self.maintenance_form)
        self.maintenance_next_maintenance_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(self.maintenance_form, text="Status:").pack(side=tk.LEFT, padx=5)
        self.maintenance_status_entry = ttk.Entry(self.maintenance_form)
        self.maintenance_status_entry.pack(side=tk.LEFT, padx=5)

    def load_maintenance_data(self):
        self.maintenance_tree.delete(*self.maintenance_tree.get_children())
        for record in self.staff_manager.maintenance_records:
            self.maintenance_tree.insert('', tk.END, values=(record.id, record.equipment_name, record.last_maintenance.strftime('%Y-%m-%d'), record.next_maintenance.strftime('%Y-%m-%d'), record.status))

    def create_buttons(self):
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill='x', pady=10)

        tk.Button(self.button_frame, text="Add Record", command=self.add_record).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Update Record", command=self.update_record).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Delete Record", command=self.delete_record).pack(side=tk.LEFT, padx=5)

    def add_record(self):
        selected_tab = self.notebook.select()
        tab_text = self.notebook.tab(selected_tab, "text")

        if tab_text == "Membership Growth":
            self.add_membership_record()
        elif tab_text == "Revenue Trends":
            self.add_revenue_record()
        elif tab_text == "Trainer Schedules":
            self.add_schedule_record()
        elif tab_text == "Equipment Maintenance":
            self.add_maintenance_record()

    def update_record(self):
        selected_tab = self.notebook.select()
        tab_text = self.notebook.tab(selected_tab, "text")

        if tab_text == "Membership Growth":
            self.update_membership_record()
        elif tab_text == "Revenue Trends":
            self.update_revenue_record()
        elif tab_text == "Trainer Schedules":
            self.update_schedule_record()
        elif tab_text == "Equipment Maintenance":
            self.update_maintenance_record()

    def delete_record(self):
        selected_tab = self.notebook.select()
        tab_text = self.notebook.tab(selected_tab, "text")

        if tab_text == "Membership Growth":
            self.delete_membership_record()
        elif tab_text == "Revenue Trends":
            self.delete_revenue_record()
        elif tab_text == "Trainer Schedules":
            self.delete_schedule_record()
        elif tab_text == "Equipment Maintenance":
            self.delete_maintenance_record()

    def add_membership_record(self):
        try:
            record = MembershipGrowth(
                id=int(self.membership_id_entry.get()),
                date=datetime.strptime(self.membership_date_entry.get(), '%Y-%m-%d'),
                new_members=int(self.membership_new_members_entry.get()),
                total_members=int(self.membership_total_members_entry.get())
            )
            self.staff_manager.add_membership_record(record)
            self.load_membership_data()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please check your entries.")

    def update_membership_record(self):
        selected_item = self.membership_tree.selection()
        if selected_item:
            try:
                item = self.membership_tree.item(selected_item)
                values = item['values']
                record_id = values[0]
                updated_record = MembershipGrowth(
                    id=record_id,
                    date=datetime.strptime(self.membership_date_entry.get(), '%Y-%m-%d'),
                    new_members=int(self.membership_new_members_entry.get()),
                    total_members=int(self.membership_total_members_entry.get())
                )
                self.staff_manager.update_membership_record(record_id, updated_record)
                self.load_membership_data()
                self.clear_membership_form()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please check your entries.")

    def delete_membership_record(self):
        selected_item = self.membership_tree.selection()
        if selected_item:
            item = self.membership_tree.item(selected_item)
            record_id = item['values'][0]
            self.staff_manager.delete_membership_record(record_id)
            self.load_membership_data()

    def add_revenue_record(self):
        try:
            record = RevenueTrends(
                id=int(self.revenue_id_entry.get()),
                date=datetime.strptime(self.revenue_date_entry.get(), '%Y-%m-%d'),
                revenue=float(self.revenue_revenue_entry.get())
            )
            self.staff_manager.add_revenue_record(record)
            self.load_revenue_data()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please check your entries.")

    def update_revenue_record(self):
        selected_item = self.revenue_tree.selection()
        if selected_item:
            try:
                item = self.revenue_tree.item(selected_item)
                values = item['values']
                record_id = values[0]
                updated_record = RevenueTrends(
                    id=record_id,
                    date=datetime.strptime(self.revenue_date_entry.get(), '%Y-%m-%d'),
                    revenue=float(self.revenue_revenue_entry.get())
                )
                self.staff_manager.update_revenue_record(record_id, updated_record)
                self.load_revenue_data()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please check your entries.")

    def delete_revenue_record(self):
        selected_item = self.revenue_tree.selection()
        if selected_item:
            item = self.revenue_tree.item(selected_item)
            record_id = item['values'][0]
            self.staff_manager.delete_revenue_record(record_id)
            self.load_revenue_data()

    def add_schedule_record(self):
        try:
            record = TrainerSchedule(
                id=int(self.schedules_id_entry.get()),
                trainer_id=int(self.schedules_trainer_id_entry.get()),
                trainer_name=self.schedules_trainer_name_entry.get(),
                class_name=self.schedules_class_name_entry.get(),
                start_time=datetime.strptime(self.schedules_start_time_entry.get(), '%H:%M:%S'),
                end_time=datetime.strptime(self.schedules_end_time_entry.get(), '%H:%M:%S')
            )
            self.staff_manager.add_schedule_record(record)
            self.load_schedules_data()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please check your entries.")

    def update_schedule_record(self):
        selected_item = self.schedules_tree.selection()
        if selected_item:
            try:
                item = self.schedules_tree.item(selected_item)
                values = item['values']
                record_id = values[0]
                updated_record = TrainerSchedule(
                    id=record_id,
                    trainer_id=int(self.schedules_trainer_id_entry.get()),
                    trainer_name=self.schedules_trainer_name_entry.get(),
                    class_name=self.schedules_class_name_entry.get(),
                    start_time=datetime.strptime(self.schedules_start_time_entry.get(), '%H:%M:%S'),
                    end_time=datetime.strptime(self.schedules_end_time_entry.get(), '%H:%M:%S')
                )
                self.staff_manager.update_schedule_record(record_id, updated_record)
                self.load_schedules_data()
                self.clear_schedules_form()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please check your entries.")

    def delete_schedule_record(self):
        selected_item = self.schedules_tree.selection()
        if selected_item:
            item = self.schedules_tree.item(selected_item)
            record_id = item['values'][0]
            self.staff_manager.delete_schedule_record(record_id)
            self.load_schedules_data()

    def add_maintenance_record(self):
        try:
            record = EquipmentMaintenance(
                id=int(self.maintenance_id_entry.get()),
                equipment_name=self.maintenance_equipment_name_entry.get(),
                last_maintenance=datetime.strptime(self.maintenance_last_maintenance_entry.get(), '%Y-%m-%d'),
                next_maintenance=datetime.strptime(self.maintenance_next_maintenance_entry.get(), '%Y-%m-%d'),
                status=self.maintenance_status_entry.get()
            )
            self.staff_manager.add_maintenance_record(record)
            self.load_maintenance_data()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please check your entries.")

    def update_maintenance_record(self):
        selected_item = self.maintenance_tree.selection()
        if selected_item:
            try:
                item = self.maintenance_tree.item(selected_item)
                values = item['values']
                record_id = values[0]
                updated_record = EquipmentMaintenance(
                    id=record_id,
                    equipment_name=self.maintenance_equipment_name_entry.get(),
                    last_maintenance=datetime.strptime(self.maintenance_last_maintenance_entry.get(), '%Y-%m-%d'),
                    next_maintenance=datetime.strptime(self.maintenance_next_maintenance_entry.get(), '%Y-%m-%d'),
                    status=self.maintenance_status_entry.get()
                )
                self.staff_manager.update_maintenance_record(record_id, updated_record)
                self.load_maintenance_data()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please check your entries.")

    # src/ui/dashboard_ui.py

    def delete_maintenance_record(self):
        selected_item = self.maintenance_tree.selection()
        if selected_item:
            item = self.maintenance_tree.item(selected_item)
            record_id = item['values'][0]
            self.staff_manager.delete_maintenance_record(record_id)
            self.load_maintenance_data()
        else:
            messagebox.showwarning("Select a record", "Please select a record to delete")