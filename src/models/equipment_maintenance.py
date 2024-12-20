# src/models/equipment_maintenance.py

from dataclasses import dataclass
from datetime import datetime

@dataclass
class EquipmentMaintenance:
    id: int
    equipment_name: str
    last_maintenance: datetime
    next_maintenance: datetime
    status: str

    @staticmethod
    def from_dict(data):
        return EquipmentMaintenance(
            id=int(data['id']),
            equipment_name=data['equipment_name'],
            last_maintenance=datetime.strptime(data['last_maintenance'], '%Y-%m-%d'),
            next_maintenance=datetime.strptime(data['next_maintenance'], '%Y-%m-%d'),
            status=data['status']
        )

    def to_dict(self):
        return {
            'id': self.id,
            'equipment_name': self.equipment_name,
            'last_maintenance': self.last_maintenance.strftime('%Y-%m-%d'),
            'next_maintenance': self.next_maintenance.strftime('%Y-%m-%d'),
            'status': self.status
        }