# tests/test_appointment_management.py

import unittest
import json
import os
from datetime import datetime
from src.models.appointment import Appointment
from src.logic.appointment_management import AppointmentManagement

class TestAppointmentManagement(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_appointments.json'
        self.sample_data = [
            {
                "appointment_id": "1",
                "member_id": "1",
                "trainer_id": "1",
                "appointment_type": "22",
                "date_time": "2001-12-12 12:12:12"
            }
        ]
        with open(self.test_file, 'w') as file:
            json.dump(self.sample_data, file, indent=4)

        self.appointment_management = AppointmentManagement(self.test_file)

    def tearDown(self):
        os.remove(self.test_file)

    def test_load_appointments(self):
        appointments = self.appointment_management.get_appointments()
        self.assertEqual(len(appointments), 1)
        self.assertEqual(appointments[0].appointment_id, "1")

    def test_add_appointment(self):
        new_appointment = Appointment(
            appointment_id="2",
            member_id="2",
            trainer_id="2",
            appointment_type="33",
            date_time=datetime.strptime("2002-12-12 12:12:12", "%Y-%m-%d %H:%M:%S")
        )
        self.appointment_management.add_appointment(new_appointment)
        appointments = self.appointment_management.get_appointments()
        self.assertEqual(len(appointments), 2)
        self.assertEqual(appointments[1].appointment_id, "2")

    def test_update_appointment(self):
        updated_appointment = Appointment(
            appointment_id="1",
            member_id="1",
            trainer_id="1",
            appointment_type="Updated",
            date_time=datetime.strptime("2001-12-12 12:12:12", "%Y-%m-%d %H:%M:%S")
        )
        result = self.appointment_management.update_appointment("1", updated_appointment)
        self.assertTrue(result)
        appointments = self.appointment_management.get_appointments()
        self.assertEqual(appointments[0].appointment_type, "Updated")

    def test_remove_appointment(self):
        self.appointment_management.remove_appointment("1")
        appointments = self.appointment_management.get_appointments()
        self.assertEqual(len(appointments), 0)

    def test_get_appointments(self):
        appointments = self.appointment_management.get_appointments()
        self.assertEqual(len(appointments), 1)
        self.assertEqual(appointments[0].appointment_id, "1")

if __name__ == '__main__':
    unittest.main()