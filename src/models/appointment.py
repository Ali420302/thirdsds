# src/models/appointment.py

from datetime import datetime

class Appointment:
    def __init__(self, appointment_id, member_id, trainer_id, appointment_type, date_time):
        self.appointment_id = appointment_id
        self.member_id = member_id
        self.trainer_id = trainer_id
        self.appointment_type = appointment_type
        self.date_time = date_time

    def to_dict(self):
        return {
            "appointment_id": self.appointment_id,
            "member_id": self.member_id,
            "trainer_id": self.trainer_id,
            "appointment_type": self.appointment_type,
            "date_time": self.date_time.strftime("%Y-%m-%d %H:%M:%S")
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["appointment_id"],
            data["member_id"],
            data["trainer_id"],
            data["appointment_type"],
            datetime.strptime(data["date_time"], "%Y-%m-%d %H:%M:%S")
        )