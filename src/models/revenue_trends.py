# src/models/revenue_trends.py

from dataclasses import dataclass
from datetime import datetime

@dataclass
class RevenueTrends:
    id: int
    date: datetime
    revenue: float

    @staticmethod
    def from_dict(data):
        return RevenueTrends(
            id=int(data['id']),
            date=datetime.strptime(data['date'], '%Y-%m-%d'),
            revenue=float(data['revenue'])
        )

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'revenue': self.revenue
        }