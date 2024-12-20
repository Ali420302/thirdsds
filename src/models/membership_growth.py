# src/models/membership_growth.py

from dataclasses import dataclass
from datetime import datetime

@dataclass
class MembershipGrowth:
    id: int
    date: datetime
    new_members: int
    total_members: int

    @staticmethod
    def from_dict(data):
        return MembershipGrowth(
            id=int(data['id']),
            date=datetime.strptime(data['date'], '%Y-%m-%d'),
            new_members=int(data['new_members']),
            total_members=int(data['total_members'])
        )

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'new_members': self.new_members,
            'total_members': self.total_members
        }