from typing import Dict, Set
from enum import Enum
from skill import Skill
from person import Person


class RoleStatus(Enum):
    Open = 0
    Closed = 1
    Need = 2


def count_matches(skills: Dict[str, Skill], required: Dict[str, Skill]) -> int:
    score = 0
    for name, skill in skills.items():
        if name in required and skill.meets(required[name]):
            score += 1
    return score


class Role():
    def __init__(self, name: str, description: str, status: RoleStatus) -> None:
        self.name: str = name
        self.description: str = description
        self.status: RoleStatus = status
        self.required_skills: Dict[str, Skill] = {}
        self.bonus_skills: Dict[str, Skill] = {}
        self.develop_skills: Dict[str, Skill] = {}
        self.appointed: Set[Person] = set()
        self.applicants: Set[Person] = set()

    def update_required_skill(self, skill: Skill) -> None:
        self.required_skills[skill.name] = skill

    def update_bonus_skill(self, skill: Skill) -> None:
        self.bonus_skills[skill.name] = skill

    def update_develop_skill(self, skill: Skill) -> None:
        self.develop_skills[skill.name] = skill

    def appoint(self, person: Person) -> None:
        self.appointed.add(person)

    def apply(self, person: Person) -> None:
        self.applicants.add(person)

    def match_score(self, person: Person) -> int:
        score = 0
        score += count_matches(person.acquired_skills, self.required_skills)
        if score != len(self.required_skills):
            return 0
        score += count_matches(person.acquired_skills, self.bonus_skills)
        score += count_matches(person.desired_skills, self.develop_skills)
        return score

    # def get_top_applicants(self) -> List[Tuple[int, Person]]:
    #     applicants: List[Tuple[int, Person]] = []
    #     for person in self.applicants

    #     return applicants

    def __str__(self):
        s = '<{}: {}> '.format(self.name, self.description)
        return s
