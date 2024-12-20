# src/logic/gym_management.py

import json
from src.models.gym_location import GymLocation

class GymManagement:
    def __init__(self, data_file):
        self.data_file = data_file
        self.gyms = self.load_gyms()

    def load_gyms(self):
        try:
            with open(self.data_file, 'r') as file:
                gyms_data = json.load(file)
                return [GymLocation.from_dict(gym) for gym in gyms_data]
        except FileNotFoundError:
            return []

    def save_gyms(self):
        with open(self.data_file, 'w') as file:
            json.dump([gym.to_dict() for gym in self.gyms], file, indent=4)

    def add_gym(self, gym):
        self.gyms.append(gym)
        self.save_gyms()

    def update_gym(self, original_location_id, updated_gym):
        for i, gym in enumerate(self.gyms):
            if gym.location_id == original_location_id:
                self.gyms[i] = updated_gym
                self.save_gyms()
                return

    def remove_gym(self, location_id):
        self.gyms = [gym for gym in self.gyms if gym.location_id != location_id]
        self.save_gyms()

    def get_gyms(self):
        return self.gyms