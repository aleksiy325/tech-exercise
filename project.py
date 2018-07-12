from typing import Dict
from enum import Enum
from role import Role
from person import Person


class ProjectStatus(Enum):
    Planning = 0
    Early = 1
    Development = 2
    Maintenance = 3
    Complete = 4


class Project():
    def __init__(self, name: str, description: str, status: ProjectStatus, owner: Person) -> None:
        self.name: str = name
        self.description: str = description
        self.status: ProjectStatus = status
        self.roles: Dict[str, Role] = {}
        self.owner = owner

    def add_role(self, role: Role) -> None:
        self.roles[role.name] = role
