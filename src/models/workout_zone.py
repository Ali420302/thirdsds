# src/models/workout_zone.py

class WorkoutZone:
    def __init__(self, zone_id, zone_type, attendant_name, updates, schedules, promotions):
        self.zone_id = zone_id
        self.zone_type = zone_type
        self.attendant_name = attendant_name
        self.updates = updates
        self.schedules = schedules
        self.promotions = promotions

    def to_dict(self):
        return {
            "zone_id": self.zone_id,
            "zone_type": self.zone_type,
            "attendant_name": self.attendant_name,
            "updates": self.updates,
            "schedules": self.schedules,
            "promotions": self.promotions
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["zone_id"],
            data["zone_type"],
            data["attendant_name"],
            data["updates"],
            data["schedules"],
            data["promotions"]
        )