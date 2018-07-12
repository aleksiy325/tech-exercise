from person import Person
from project import Project
from role import Role
from skill import Skill


class Endorsement():
    def __init__(self, rating: int, feedback: str, skill: Skill, project: Project, role: Role, endorser: Person, endorsed: Person) -> None:
        self.rating: int = rating
        self.feedback: str = feedback
        self.skill: Skill = skill
        self.project: Project = project
        self.role: Role = role
        self.endorser: Person = endorser
        self.endorsed: Person = endorsed
