from typing import Dict, Set, List, Tuple
from enum import Enum
from skill import Skill
from person import Person
from endorsement import Endorsement


class RoleStatus(Enum):
    Open = 0
    Closed = 1
    Need = 2


def calc_score(skills: Dict[str, Skill], endorsements: Dict[str, List[Endorsement]], required: Dict[str, Skill]):
    score = 0
    for name, skill in skills.items():
        if name in required:
            score += skill.experience_rating
    for name, endorsement_list in endorsements.items():
        if name in required:
            for endorsement in endorsement_list:
                score += endorsement.skill.experience_rating
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

    def accept(self, person: Person) -> None:
        self.appointed.add(person)
        if person in self.applicants:
            self.applicants.remove(person)

    def deny(self, person: Person) -> None:
        if person in self.applicants:
            self.applicants.remove(person)

    def apply(self, person: Person) -> None:
        self.applicants.add(person)

    def match_score(self, person: Person) -> int:
        score = 0
        score += calc_score(person.acquired_skills,
                            person.received_endorsements,  self.required_skills)
        score += calc_score(person.acquired_skills,
                            person.received_endorsements, self.bonus_skills)
        score += calc_score(person.desired_skills, {}, self.develop_skills)
        return score

    def get_top_applicants(self) -> List[Tuple[int, Person]]:
        top: List[Tuple[int, Person]] = []
        for person in self.applicants:
            top.append((self.match_score(person), person))
        top = sorted(top, key=lambda x: x[0], reverse=True)
        return top

    def __str__(self):
        s = '{}: {} '.format(self.name, self.description)
        return s

    def print_role(self):
        print(self.name)
        print(self.description)
        print('Required Skills: ' + ', '.join([str(skill)
                                               for skill in self.required_skills.values()]))
        print('Bonus Skills: ' + ', '.join([str(skill)
                                            for skill in self.bonus_skills.values()]))
        print('Will Develop Skills: ' + ', '.join([str(skill)
                                                   for skill in self.develop_skills.values()]))
        print('\n')
