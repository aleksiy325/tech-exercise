from typing import Dict
from skill import Skill


class Role():
    def __init__(self, name: str, description: str, status: int) -> None:
        self.name: str = name
        self.description: str = description
        self.status: int = status
        self.required_skills: Dict[str, Skill] = {}
        self.bonus_skills: Dict[str, Skill] = {}
        self.develop_skills: Dict[str, Skill] = {}
