from typing import Dict, List
from skill import Skill
from endorsement import Endorsement


class Person():
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.acquired_skills: Dict[str, Skill] = {}
        self.desired_skills: Dict[str, Skill] = {}
        self.received_endorsements: Dict[str, List[Endorsement]] = {}
        self.given_endorsements: Dict[str, List[Endorsement]] = {}

    def update_acquired_skill(self, skill: Skill) -> None:
        self.acquired_skills[skill.name] = skill

    def update_desired_skill(self, skill: Skill) -> None:
        self.desired_skills[skill.name] = skill

    def endorse(self, endorsement: Endorsement, endorser) -> None:
        self.received_endorsements.setdefault(
            endorsement.skill.name, []).append(endorsement)
        endorser.given_endorsements.setdefault(
            endorsement.skill.name, []).append(endorsement)

    def __str__(self):
        s = '{} {}'.format(self.first_name, self.last_name)
        return s

    def print_profile(self):
        print('{} {}'.format(self.first_name, self.last_name))
        print('Acquired Skills: ' + ', '.join([str(skill)
                                               for skill in self.acquired_skills.values()]))
        print('Desired Skills: ' + ', '.join([str(skill)
                                              for skill in self.desired_skills.values()]))
        print('Endorsements: ' + ', '.join([str(endorsement)
                                            for endorsements in self.received_endorsements.values() for endorsement in endorsements]))
        print('\n')
