# src/logic/workout_zone_management.py

import json
from src.models.workout_zone import WorkoutZone

class WorkoutZoneManagement:
    def __init__(self, data_file):
        self.data_file = data_file
        self.zones = self.load_zones()

    def load_zones(self):
        try:
            with open(self.data_file, 'r') as file:
                zones_data = json.load(file)
                return [WorkoutZone.from_dict(zone) for zone in zones_data]
        except FileNotFoundError:
            return []

    def save_zones(self):
        with open(self.data_file, 'w') as file:
            json.dump([zone.to_dict() for zone in self.zones], file, indent=4)

    def add_zone(self, zone):
        self.zones.append(zone)
        self.save_zones()

    def update_zone(self, original_zone_id, updated_zone):
        for i, zone in enumerate(self.zones):
            if zone.zone_id == original_zone_id:
                self.zones[i] = updated_zone
                self.save_zones()
                return

    def remove_zone(self, zone_id):
        self.zones = [zone for zone in self.zones if zone.zone_id != zone_id]
        self.save_zones()

    def get_zones(self):
        return self.zones