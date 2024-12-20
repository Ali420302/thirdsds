# src/models/trainer_schedules.py

from dataclasses import dataclass
from datetime import datetime

@dataclass
class TrainerSchedule:
    id: int
    trainer_id: int
    trainer_name: str
    class_name: str
    start_time: datetime
    end_time: datetime

    @staticmethod
    def from_dict(data):
        return TrainerSchedule(
            id=int(data['id']),
            trainer_id=int(data['trainer_id']),
            trainer_name=data['trainer_name'],
            class_name=data['class_name'],
            start_time=datetime.strptime(data['start_time'], '%H:%M:%S'),
            end_time=datetime.strptime(data['end_time'], '%H:%M:%S')
        )

    def to_dict(self):
        return {
            'id': self.id,
            'trainer_id': self.trainer_id,
            'trainer_name': self.trainer_name,
            'class_name': self.class_name,
            'start_time': self.start_time.strftime('%H:%M:%S'),
            'end_time': self.end_time.strftime('%H:%M:%S')
        }