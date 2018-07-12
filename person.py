from typing import Dict, List
from skill import Skill


class Person():
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.acquired_skills: Dict[str, Skill] = {}
        self.desired_skills: Dict[str, Skill] = {}

    def update_acquired_skill(self, skill: Skill) -> None:
        self.acquired_skills[skill.name] = skill

    def update_desired_skill(self, skill: Skill) -> None:
        self.desired_skills[skill.name] = skill

    def __str__(self):
        s = '{} {}'.format(self.first_name, self.last_name)
        return s
