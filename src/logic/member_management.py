# src/logic/member_management.py

import json
from src.models.member import Member

class MemberManagement:
    def __init__(self, data_file):
        self.data_file = data_file
        self.members = self.load_members()

    def load_members(self):
        try:
            with open(self.data_file, 'r') as file:
                members_data = json.load(file)
                return [Member.from_dict(member) for member in members_data]
        except FileNotFoundError:
            return []

    def save_members(self):
        with open(self.data_file, 'w') as file:
            json.dump([member.to_dict() for member in self.members], file, indent=4)

    def add_member(self, member):
        self.members.append(member)
        self.save_members()

    def update_member(self, member_id, updated_member):
        for i, member in enumerate(self.members):
            if member.member_id == member_id:
                self.members[i] = updated_member
                self.save_members()
                return True
        return False

    def remove_member(self, member_id):
        self.members = [member for member in self.members if member.member_id != member_id]
        self.save_members()

    def get_members(self):
        return self.members