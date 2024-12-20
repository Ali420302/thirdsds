# src/models/gym_location.py

class GymLocation:
    def __init__(self, location_id, city, manager_name, workout_zones, equipment, amenities):
        self.location_id = location_id
        self.city = city
        self.manager_name = manager_name
        self.workout_zones = workout_zones
        self.equipment = equipment
        self.amenities = amenities

    def to_dict(self):
        return {
            "location_id": self.location_id,
            "city": self.city,
            "manager_name": self.manager_name,
            "workout_zones": self.workout_zones,
            "equipment": self.equipment,
            "amenities": self.amenities
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["location_id"],
            data["city"],
            data["manager_name"],
            data["workout_zones"],
            data["equipment"],
            data["amenities"]
        )