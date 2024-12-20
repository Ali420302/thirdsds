# src/logic/attendance_management.py

import json
from datetime import datetime
from src.models.attendance import Attendance

class AttendanceManagement:
    def __init__(self, data_file):
        self.data_file = data_file
        self.attendances = self.load_attendances()

    def load_attendances(self):
        try:
            with open(self.data_file, 'r') as file:
                attendances_data = json.load(file)
                return [Attendance.from_dict(attendance) for attendance in attendances_data]
        except FileNotFoundError:
            return []

    def save_attendances(self):
        with open(self.data_file, 'w') as file:
            json.dump([attendance.to_dict() for attendance in self.attendances], file, indent=4)

    def add_attendance(self, attendance):
        self.attendances.append(attendance)
        self.save_attendances()

    def update_attendance(self, attendance_id, updated_attendance):
        for i, attendance in enumerate(self.attendances):
            if attendance.attendance_id == attendance_id:
                self.attendances[i] = updated_attendance
                self.save_attendances()
                return True
        return False

    def remove_attendance(self, attendance_id):
        self.attendances = [attendance for attendance in self.attendances if attendance.attendance_id != attendance_id]
        self.save_attendances()

    def get_attendances(self):
        return self.attendances

    def get_attendance_by_member(self, member_id):
        return [attendance for attendance in self.attendances if attendance.member_id == member_id]

    def get_attendance_by_class(self, class_id):
        return [attendance for attendance in self.attendances if attendance.class_id == class_id]

    def get_peak_hours(self):
        hours = [0] * 24
        for attendance in self.attendances:
            check_in_hour = attendance.check_in_time.hour
            hours[check_in_hour] += 1
        return hours