# src/models/member.py

class Member:
    def __init__(self, member_id, name, age, health_info, membership_status):
        self.member_id = member_id
        self.name = name
        self.age = age
        self.health_info = health_info
        self.membership_status = membership_status

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "age": self.age,
            "health_info": self.health_info,
            "membership_status": self.membership_status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["member_id"],
            data["name"],
            data["age"],
            data["health_info"],
            data["membership_status"]
        )