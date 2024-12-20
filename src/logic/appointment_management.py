# src/logic/appointment_management.py

import json
from datetime import datetime
from src.models.appointment import Appointment

class AppointmentManagement:
    def __init__(self, data_file):
        self.data_file = data_file
        self.appointments = self.load_appointments()

    def load_appointments(self):
        try:
            with open(self.data_file, 'r') as file:
                appointments_data = json.load(file)
                return [Appointment.from_dict(appointment) for appointment in appointments_data]
        except FileNotFoundError:
            return []

    def save_appointments(self):
        with open(self.data_file, 'w') as file:
            json.dump([appointment.to_dict() for appointment in self.appointments], file, indent=4)

    def add_appointment(self, appointment):
        self.appointments.append(appointment)
        self.save_appointments()

    def update_appointment(self, appointment_id, updated_appointment):
        for i, appointment in enumerate(self.appointments):
            if appointment.appointment_id == appointment_id:
                self.appointments[i] = updated_appointment
                self.save_appointments()
                return True
        return False

    def remove_appointment(self, appointment_id):
        self.appointments = [appointment for appointment in self.appointments if appointment.appointment_id != appointment_id]
        self.save_appointments()

    def get_appointments(self):
        return self.appointments