# src/ui/workout_zone_ui.py

import tkinter as tk
from tkinter import messagebox

from src.config import DATA_FILE_WORKOUT_ZONE
from src.logic.workout_zone_management import WorkoutZoneManagement
from src.models.workout_zone import WorkoutZone


class WorkoutZoneManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Workout Zone Management System")
        self.zone_management = WorkoutZoneManagement(data_file=DATA_FILE_WORKOUT_ZONE)

        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Workout Zone Management", font=("Helvetica", 16)).pack(pady=10)

        # Workout Zone Form
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(pady=10)

        tk.Label(self.form_frame, text="Zone ID:").grid(row=0, column=0, padx=5, pady=5)
        self.zone_id_entry = tk.Entry(self.form_frame)
        self.zone_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Zone Type:").grid(row=1, column=0, padx=5, pady=5)
        self.zone_type_entry = tk.Entry(self.form_frame)
        self.zone_type_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Attendant Name:").grid(row=2, column=0, padx=5, pady=5)
        self.attendant_entry = tk.Entry(self.form_frame)
        self.attendant_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Updates:").grid(row=3, column=0, padx=5, pady=5)
        self.updates_entry = tk.Entry(self.form_frame)
        self.updates_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Schedules:").grid(row=4, column=0, padx=5, pady=5)
        self.schedules_entry = tk.Entry(self.form_frame)
        self.schedules_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Promotions:").grid(row=5, column=0, padx=5, pady=5)
        self.promotions_entry = tk.Entry(self.form_frame)
        self.promotions_entry.grid(row=5, column=1, padx=5, pady=5)

        button_frame = tk.Frame(self.form_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=10)

        tk.Button(button_frame, text="Add Zone", command=self.add_zone).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Update Zone", command=self.update_zone).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remove Zone", command=self.remove_zone).pack(side=tk.LEFT, padx=5)

        # Workout Zones List
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(pady=10)

        self.zone_listbox = tk.Listbox(self.list_frame, width=50, height=10)
        self.zone_listbox.pack(side=tk.LEFT, padx=10)
        self.update_zone_listbox()

        scrollbar = tk.Scrollbar(self.list_frame, orient="vertical")
        scrollbar.config(command=self.zone_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.zone_listbox.config(yscrollcommand=scrollbar.set)

    def add_zone(self):
        zone_id = self.zone_id_entry.get()
        zone_type = self.zone_type_entry.get()
        attendant_name = self.attendant_entry.get()
        updates = self.updates_entry.get()
        schedules = self.schedules_entry.get()
        promotions = self.promotions_entry.get()

        if not zone_id or not zone_type or not attendant_name:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        zone = WorkoutZone(zone_id, zone_type, attendant_name, updates, schedules, promotions)
        self.zone_management.add_zone(zone)
        self.update_zone_listbox()
        self.clear_form()

    def update_zone(self):
        selected_index = self.zone_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a zone to update")
            return

        zone_id = self.zone_id_entry.get()
        zone_type = self.zone_type_entry.get()
        attendant_name = self.attendant_entry.get()
        updates = self.updates_entry.get()
        schedules = self.schedules_entry.get()
        promotions = self.promotions_entry.get()

        if not zone_id or not zone_type or not attendant_name:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        selected_zone = self.zone_listbox.get(selected_index)
        original_zone_id = selected_zone.split(" - ")[0]

        zone = WorkoutZone(zone_id, zone_type, attendant_name, updates, schedules, promotions)
        self.zone_management.update_zone(original_zone_id, zone)
        self.update_zone_listbox()
        self.clear_form()

    def remove_zone(self):
        selected_index = self.zone_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a zone to remove")
            return

        selected_zone = self.zone_listbox.get(selected_index)
        zone_id = selected_zone.split(" - ")[0]

        self.zone_management.remove_zone(zone_id)
        self.update_zone_listbox()

    def update_zone_listbox(self):
        self.zone_listbox.delete(0, tk.END)
        for zone in self.zone_management.get_zones():
            self.zone_listbox.insert(tk.END, f"{zone.zone_id} - {zone.zone_type} - {zone.attendant_name}")

    def clear_form(self):
        self.zone_id_entry.delete(0, tk.END)
        self.zone_type_entry.delete(0, tk.END)
        self.attendant_entry.delete(0, tk.END)
        self.updates_entry.delete(0, tk.END)
        self.schedules_entry.delete(0, tk.END)
        self.promotions_entry.delete(0, tk.END)

