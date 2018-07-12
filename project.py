from typing import Dict
from role import Role


class Project():
    def __init__(self, name: str, description: str) -> None:
        self.name: str = name
        self.description: str = description
        self.roles: Dict[str, Role] = {}
