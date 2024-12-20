# src/staff_management/staff_manager.py

import json
from src.models.membership_growth import MembershipGrowth
from src.models.revenue_trends import RevenueTrends
from src.models.trainer_schedules import TrainerSchedule
from src.models.equipment_maintenance import EquipmentMaintenance

class StaffManager:
    def __init__(self, membership_file, revenue_file, schedules_file, maintenance_file):
        self.membership_file = membership_file
        self.revenue_file = revenue_file
        self.schedules_file = schedules_file
        self.maintenance_file = maintenance_file

        self.membership_records = self.load_membership_records()
        self.revenue_records = self.load_revenue_records()
        self.schedules_records = self.load_schedules_records()
        self.maintenance_records = self.load_maintenance_records()

    def load_membership_records(self):
        with open(self.membership_file, 'r') as file:
            data = json.load(file)
        return [MembershipGrowth.from_dict(item) for item in data]

    def save_membership_records(self):
        data = [record.to_dict() for record in self.membership_records]
        with open(self.membership_file, 'w') as file:
            json.dump(data, file, indent=4)

    def add_membership_record(self, record):
        self.membership_records.append(record)
        self.save_membership_records()

    def update_membership_record(self, record_id, updated_record):
        for i, record in enumerate(self.membership_records):
            if record.id == record_id:
                self.membership_records[i] = updated_record
                self.save_membership_records()
                return True
        return False

    def delete_membership_record(self, record_id):
        self.membership_records = [record for record in self.membership_records if record.id != record_id]
        self.save_membership_records()

    def load_revenue_records(self):
        with open(self.revenue_file, 'r') as file:
            data = json.load(file)
        return [RevenueTrends.from_dict(item) for item in data]

    def save_revenue_records(self):
        data = [record.to_dict() for record in self.revenue_records]
        with open(self.revenue_file, 'w') as file:
            json.dump(data, file, indent=4)

    def add_revenue_record(self, record):
        self.revenue_records.append(record)
        self.save_revenue_records()

    def update_revenue_record(self, record_id, updated_record):
        for i, record in enumerate(self.revenue_records):
            if record.id == record_id:
                self.revenue_records[i] = updated_record
                self.save_revenue_records()
                return True
        return False

    def delete_revenue_record(self, record_id):
        self.revenue_records = [record for record in self.revenue_records if record.id != record_id]
        self.save_revenue_records()

    def load_schedules_records(self):
        with open(self.schedules_file, 'r') as file:
            data = json.load(file)
        return [TrainerSchedule.from_dict(item) for item in data]

    def save_schedules_records(self):
        data = [record.to_dict() for record in self.schedules_records]
        with open(self.schedules_file, 'w') as file:
            json.dump(data, file, indent=4)

    def add_schedule_record(self, record):
        self.schedules_records.append(record)
        self.save_schedules_records()

    def update_schedule_record(self, record_id, updated_record):
        for i, record in enumerate(self.schedules_records):
            if record.id == record_id:
                self.schedules_records[i] = updated_record
                self.save_schedules_records()
                return True
        return False

    def delete_schedule_record(self, record_id):
        self.schedules_records = [record for record in self.schedules_records if record.id != record_id]
        self.save_schedules_records()

    def load_maintenance_records(self):
        with open(self.maintenance_file, 'r') as file:
            data = json.load(file)
        return [EquipmentMaintenance.from_dict(item) for item in data]

    def save_maintenance_records(self):
        data = [record.to_dict() for record in self.maintenance_records]
        with open(self.maintenance_file, 'w') as file:
            json.dump(data, file, indent=4)

    def add_maintenance_record(self, record):
        self.maintenance_records.append(record)
        self.save_maintenance_records()

    def update_maintenance_record(self, record_id, updated_record):
        for i, record in enumerate(self.maintenance_records):
            if record.id == record_id:
                self.maintenance_records[i] = updated_record
                self.save_maintenance_records()
                return True
        return False

    def delete_maintenance_record(self, record_id):
        self.maintenance_records = [record for record in self.maintenance_records if record.id != record_id]
        self.save_maintenance_records()