# src/ui/gym_management_ui.py

import tkinter as tk
from tkinter import messagebox

from src.config import DATA_FILE_GYM
from src.logic.gym_management import GymManagement
from src.models.gym_location import GymLocation


class GymManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Management System")
        self.gym_management = GymManagement(data_file=DATA_FILE_GYM)

        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Gym Management", font=("Helvetica", 16)).pack(pady=10)

        # Gym Location Form
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(pady=10)

        tk.Label(self.form_frame, text="Location ID:").grid(row=0, column=0, padx=5, pady=5)
        self.location_id_entry = tk.Entry(self.form_frame)
        self.location_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="City:").grid(row=1, column=0, padx=5, pady=5)
        self.city_entry = tk.Entry(self.form_frame)
        self.city_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Manager Name:").grid(row=2, column=0, padx=5, pady=5)
        self.manager_entry = tk.Entry(self.form_frame)
        self.manager_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Workout Zones:").grid(row=3, column=0, padx=5, pady=5)
        self.zones_entry = tk.Entry(self.form_frame)
        self.zones_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Equipment:").grid(row=4, column=0, padx=5, pady=5)
        self.equipment_entry = tk.Entry(self.form_frame)
        self.equipment_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Amenities:").grid(row=5, column=0, padx=5, pady=5)
        self.amenities_entry = tk.Entry(self.form_frame)
        self.amenities_entry.grid(row=5, column=1, padx=5, pady=5)

        button_frame = tk.Frame(self.form_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=10)

        tk.Button(button_frame, text="Add Gym", command=self.add_gym).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Update Gym", command=self.update_gym).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remove Gym", command=self.remove_gym).pack(side=tk.LEFT, padx=5)

        # Gym Locations List
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(pady=10)

        self.gym_listbox = tk.Listbox(self.list_frame, width=50, height=10)
        self.gym_listbox.pack(side=tk.LEFT, padx=10)
        self.update_gym_listbox()

        scrollbar = tk.Scrollbar(self.list_frame, orient="vertical")
        scrollbar.config(command=self.gym_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.gym_listbox.config(yscrollcommand=scrollbar.set)

    def add_gym(self):
        location_id = self.location_id_entry.get()
        city = self.city_entry.get()
        manager_name = self.manager_entry.get()
        workout_zones = self.zones_entry.get()
        equipment = self.equipment_entry.get()
        amenities = self.amenities_entry.get()

        if not location_id or not city or not manager_name:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        gym = GymLocation(location_id, city, manager_name, workout_zones, equipment, amenities)
        self.gym_management.add_gym(gym)
        self.update_gym_listbox()
        self.clear_form()

    def update_gym(self):
        selected_index = self.gym_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a gym to update")
            return

        location_id = self.location_id_entry.get()
        city = self.city_entry.get()
        manager_name = self.manager_entry.get()
        workout_zones = self.zones_entry.get()
        equipment = self.equipment_entry.get()
        amenities = self.amenities_entry.get()

        if not location_id or not city or not manager_name:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        selected_gym = self.gym_listbox.get(selected_index)
        original_location_id = selected_gym.split(" - ")[0]

        gym = GymLocation(location_id, city, manager_name, workout_zones, equipment, amenities)
        self.gym_management.update_gym(original_location_id, gym)
        self.update_gym_listbox()
        self.clear_form()

    def remove_gym(self):
        selected_index = self.gym_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a gym to remove")
            return

        selected_gym = self.gym_listbox.get(selected_index)
        location_id = selected_gym.split(" - ")[0]

        self.gym_management.remove_gym(location_id)
        self.update_gym_listbox()

    def update_gym_listbox(self):
        self.gym_listbox.delete(0, tk.END)
        for gym in self.gym_management.get_gyms():
            self.gym_listbox.insert(tk.END, f"{gym.location_id} - {gym.city} - {gym.manager_name}")

    def clear_form(self):
        self.location_id_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        self.manager_entry.delete(0, tk.END)
        self.zones_entry.delete(0, tk.END)
        self.equipment_entry.delete(0, tk.END)
        self.amenities_entry.delete(0, tk.END)

