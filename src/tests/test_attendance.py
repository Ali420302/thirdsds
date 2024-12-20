# tests/test_attendance_management.py

import unittest
import json
import os
from datetime import datetime
from src.models.attendance import Attendance
from src.logic.attendance_management import AttendanceManagement

class TestAttendanceManagement(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_attendances.json'
        self.sample_data = [
            {
                "attendance_id": "1",
                "member_id": "1",
                "class_id": "101",
                "check_in_time": "2024-12-20 08:00:00",
                "check_out_time": "2024-12-20 09:00:00"
            }
        ]
        with open(self.test_file, 'w') as file:
            json.dump(self.sample_data, file, indent=4)

        self.attendance_management = AttendanceManagement(self.test_file)

    def tearDown(self):
        os.remove(self.test_file)

    def test_load_attendances(self):
        attendances = self.attendance_management.get_attendances()
        self.assertEqual(len(attendances), 1)
        self.assertEqual(attendances[0].attendance_id, "1")

    def test_add_attendance(self):
        new_attendance = Attendance(
            attendance_id="2",
            member_id="2",
            class_id="102",
            check_in_time=datetime.strptime("2024-12-20 10:00:00", "%Y-%m-%d %H:%M:%S"),
            check_out_time=datetime.strptime("2024-12-20 11:00:00", "%Y-%m-%d %H:%M:%S")
        )
        self.attendance_management.add_attendance(new_attendance)
        attendances = self.attendance_management.get_attendances()
        self.assertEqual(len(attendances), 2)
        self.assertEqual(attendances[1].attendance_id, "2")

    def test_update_attendance(self):
        updated_attendance = Attendance(
            attendance_id="1",
            member_id="1",
            class_id="101",
            check_in_time=datetime.strptime("2024-12-20 08:00:00", "%Y-%m-%d %H:%M:%S"),
            check_out_time=datetime.strptime("2024-12-20 10:00:00", "%Y-%m-%d %H:%M:%S")
        )
        result = self.attendance_management.update_attendance("1", updated_attendance)
        self.assertTrue(result)
        attendances = self.attendance_management.get_attendances()
        self.assertEqual(attendances[0].check_out_time, datetime.strptime("2024-12-20 10:00:00", "%Y-%m-%d %H:%M:%S"))

    def test_remove_attendance(self):
        self.attendance_management.remove_attendance("1")
        attendances = self.attendance_management.get_attendances()
        self.assertEqual(len(attendances), 0)

    def test_get_attendances(self):
        attendances = self.attendance_management.get_attendances()
        self.assertEqual(len(attendances), 1)
        self.assertEqual(attendances[0].attendance_id, "1")

    def test_get_attendance_by_member(self):
        attendances = self.attendance_management.get_attendance_by_member("1")
        self.assertEqual(len(attendances), 1)
        self.assertEqual(attendances[0].member_id, "1")

    def test_get_attendance_by_class(self):
        attendances = self.attendance_management.get_attendance_by_class("101")
        self.assertEqual(len(attendances), 1)
        self.assertEqual(attendances[0].class_id, "101")

    def test_get_peak_hours(self):
        peak_hours = self.attendance_management.get_peak_hours()
        self.assertEqual(peak_hours[8], 1)
        self.assertEqual(sum(peak_hours), 1)  # Ensure only one check-in is counted

if __name__ == '__main__':
    unittest.main()