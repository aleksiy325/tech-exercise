from typing import List, Tuple
from person import Person
from skill import Skill
from project import Project, ProjectStatus
from role import Role, RoleStatus
from enum import Enum


class Skills(Enum):
    Leadership = "Leadership"
    Martial = "Martial"
    Financial = "Financial"
    Oratory = "Oratory"
    Charisma = "Charisma"
    Administration = "Administration"


class Roles(Enum):
    Commander = "Commander"
    Consul = "Consul"


def get_top_roles(person: Person, projects: List[Project]) -> List[Tuple[int, Role]]:
    scores: List[Tuple[int, Role]] = []
    for project in projects:
        for role in project.roles.values():
            scores.append((role.match_score(person), role))
    scores = sorted(scores, key=lambda x: x[0], reverse=True)
    return scores


def print_top_roles(person: Person, projects: List[Project]) -> None:
    print('Top Roles for {}'.format(person))
    for score, role in get_top_roles(person, projects):
        print(score, role)


projects: List[Project] = []

julius_caesar = Person("Julius", "Caesar")
julius_caesar.update_acquired_skill(Skill(str(Skills.Leadership), 8))
julius_caesar.update_acquired_skill(Skill(str(Skills.Martial), 6))
julius_caesar.update_acquired_skill(Skill(str(Skills.Charisma), 9))

julius_caesar.update_desired_skill(Skill(str(Skills.Administration), 5))
julius_caesar.update_desired_skill(Skill(str(Skills.Financial), 5))

markus_crassus = Person("Markus", "Crassus")
markus_crassus.update_acquired_skill(Skill(str(Skills.Leadership), 6))
markus_crassus.update_acquired_skill(Skill(str(Skills.Financial), 8))
markus_crassus.update_acquired_skill(Skill(str(Skills.Administration), 7))

markus_crassus.update_desired_skill(Skill(str(Skills.Martial), 6))
markus_crassus.update_desired_skill(Skill(str(Skills.Charisma), 6))
markus_crassus.update_desired_skill(Skill(str(Skills.Oratory), 6))


pompey_magnus = Person("Pompey", "Magnus")
pompey_magnus.update_acquired_skill(Skill(str(Skills.Leadership), 8))
pompey_magnus.update_acquired_skill(Skill(str(Skills.Martial), 6))
pompey_magnus.update_acquired_skill(Skill(str(Skills.Administration), 8))


pompey_magnus.update_desired_skill(Skill(str(Skills.Leadership), 10))
pompey_magnus.update_desired_skill(Skill(str(Skills.Administration), 10))


marcus_cicero = Person("Markus", "Cicero")
marcus_cicero.update_acquired_skill(Skill(str(Skills.Leadership), 3))
marcus_cicero.update_acquired_skill(Skill(str(Skills.Oratory), 9))

govern_rome = Project(
    "Govern Rome", "Project to govern the city.",
    ProjectStatus.Maintenance,
    marcus_cicero)

consul = Role(str(Roles.Consul),
              "Serve as one of two Consuls of Rome.", RoleStatus.Open)
consul.update_required_skill(Skill(str(Skills.Leadership), 6))
consul.update_required_skill(Skill(str(Skills.Administration), 6))

consul.update_bonus_skill(Skill(str(Skills.Financial), 8))
consul.update_bonus_skill(Skill(str(Skills.Charisma), 6))
consul.update_bonus_skill(Skill(str(Skills.Oratory), 4))

consul.update_develop_skill(Skill(str(Skills.Financial), 0))
consul.update_develop_skill(Skill(str(Skills.Leadership), 0))
consul.update_develop_skill(Skill(str(Skills.Administration), 0))
govern_rome.add_role(consul)

projects.append(govern_rome)

marc_antony = Person("Marcus", "Antonius")
marc_antony.update_acquired_skill(Skill(str(Skills.Martial), 6))
marc_antony.update_acquired_skill(Skill(str(Skills.Leadership), 6))

gaul_campaign = Project(
    "Gallic Campaign",
    "Campaign to conquer gaul.",
    ProjectStatus.Planning,
    marc_antony)
command = Role(str(Roles.Commander), "Command campaign.", RoleStatus.Open)
command.update_required_skill(Skill(str(Skills.Martial), 4))
command.update_bonus_skill(Skill(str(Skills.Leadership), 4))
command.update_bonus_skill(Skill(str(Skills.Martial), 6))
command.update_develop_skill(Skill(str(Skills.Martial), 0))
command.update_develop_skill(Skill(str(Skills.Leadership), 0))

gaul_campaign.add_role(command)
projects.append(gaul_campaign)

print_top_roles(pompey_magnus, projects)
print_top_roles(markus_crassus, projects)
print_top_roles(julius_caesar, projects)
print_top_roles(marc_antony, projects)
print_top_roles(marcus_cicero, projects)
