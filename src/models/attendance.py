# src/models/attendance.py

from datetime import datetime

class Attendance:
    def __init__(self, attendance_id, member_id, class_id, check_in_time, check_out_time=None):
        self.attendance_id = attendance_id
        self.member_id = member_id
        self.class_id = class_id
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time

    def to_dict(self):
        return {
            "attendance_id": self.attendance_id,
            "member_id": self.member_id,
            "class_id": self.class_id,
            "check_in_time": self.check_in_time.strftime("%Y-%m-%d %H:%M:%S"),
            "check_out_time": self.check_out_time.strftime("%Y-%m-%d %H:%M:%S") if self.check_out_time else None
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["attendance_id"],
            data["member_id"],
            data["class_id"],
            datetime.strptime(data["check_in_time"], "%Y-%m-%d %H:%M:%S"),
            datetime.strptime(data["check_out_time"], "%Y-%m-%d %H:%M:%S") if data["check_out_time"] else None
        )