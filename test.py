from typing import List, Tuple
from person import Person
from skill import Skill
from project import Project, ProjectStatus
from role import Role, RoleStatus
from endorsement import Endorsement
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
    Dictator = "Dictator"


def get_top_roles(person: Person, projects: List[Project]) -> List[Tuple[int, Role]]:
    scores = []
    for project in projects:
        for role in project.roles.values():
            scores.append((role.match_score(person), role))
    scores = sorted(scores, key=lambda x: x[0], reverse=True)
    return scores


def print_top_roles(person: Person, projects: List[Project]) -> None:
    print('Top Roles for {}'.format(person))
    for score, role in get_top_roles(person, projects):
        print(score, role)


def select_and_print(role: Role, open: int) -> None:
    print('Selection for {}'.format(role))
    for i, (score, person) in enumerate(role.get_top_applicants()):
        decision = "Deny"
        if i < open:
            decision = "Accept"
            role.accept(person)
        else:
            role.deny(person)
        print("{} {} {} for {}".format(decision, score, person, role))


projects: List[Project] = []

julius_caesar = Person("Julius", "Caesar")
julius_caesar.update_acquired_skill(Skill(Skills.Leadership.name, 6))
julius_caesar.update_acquired_skill(Skill(Skills.Martial.name, 6))
julius_caesar.update_acquired_skill(Skill(Skills.Charisma.name, 7))

julius_caesar.update_desired_skill(Skill(Skills.Administration.name, 5))
julius_caesar.update_desired_skill(Skill(Skills.Financial.name, 5))
julius_caesar.update_desired_skill(Skill(Skills.Martial.name, 8))


markus_crassus = Person("Markus", "Crassus")
markus_crassus.update_acquired_skill(Skill(Skills.Leadership.name, 6))
markus_crassus.update_acquired_skill(Skill(Skills.Financial.name, 8))
markus_crassus.update_acquired_skill(Skill(Skills.Administration.name, 8))

markus_crassus.update_desired_skill(Skill(Skills.Martial.name, 6))
markus_crassus.update_desired_skill(Skill(Skills.Charisma.name, 6))
markus_crassus.update_desired_skill(Skill(Skills.Oratory.name, 6))


pompey_magnus = Person("Pompey", "Magnus")
pompey_magnus.update_acquired_skill(Skill(Skills.Leadership.name, 8))
pompey_magnus.update_acquired_skill(Skill(Skills.Martial.name, 6))
pompey_magnus.update_acquired_skill(Skill(Skills.Administration.name, 8))


pompey_magnus.update_desired_skill(Skill(Skills.Leadership.name, 10))
pompey_magnus.update_desired_skill(Skill(Skills.Administration.name, 10))


marcus_cicero = Person("Markus", "Cicero")
marcus_cicero.update_acquired_skill(Skill(Skills.Leadership.name, 3))
marcus_cicero.update_acquired_skill(Skill(Skills.Oratory.name, 9))

govern_rome = Project(
    "Govern Rome", "Project to govern the city.",
    ProjectStatus.Maintenance,
    marcus_cicero)

consul = Role(Roles.Consul.name,
              "Serve as one of two Consuls of Rome.", RoleStatus.Open)
consul.update_required_skill(Skill(Skills.Leadership.name, 6))
consul.update_required_skill(Skill(Skills.Administration.name, 6))
consul.update_required_skill(Skill(Skills.Financial.name, 6))


consul.update_bonus_skill(Skill(Skills.Financial.name, 8))
consul.update_bonus_skill(Skill(Skills.Charisma.name, 6))
consul.update_bonus_skill(Skill(Skills.Oratory.name, 4))
consul.update_bonus_skill(Skill(Skills.Martial.name, 5))

consul.update_develop_skill(Skill(Skills.Financial.name, 0))
consul.update_develop_skill(Skill(Skills.Leadership.name, 0))
consul.update_develop_skill(Skill(Skills.Administration.name, 0))
govern_rome.add_role(consul)

projects.append(govern_rome)

marc_antony = Person("Marcus", "Antonius")
marc_antony.update_acquired_skill(Skill(Skills.Martial.name, 6))
marc_antony.update_acquired_skill(Skill(Skills.Leadership.name, 6))

gaul_campaign = Project(
    "Gallic Campaign",
    "Campaign to conquer Gaul.",
    ProjectStatus.Planning,
    marc_antony)

command = Role(Roles.Commander.name,
               "Command Gallic campaign.", RoleStatus.Open)
command.update_required_skill(Skill(Skills.Martial.name, 4))
command.update_bonus_skill(Skill(Skills.Leadership.name, 4))
command.update_bonus_skill(Skill(Skills.Martial.name, 6))
command.update_develop_skill(Skill(Skills.Martial.name, 0))
command.update_develop_skill(Skill(Skills.Leadership.name, 0))

gaul_campaign.add_role(command)
projects.append(gaul_campaign)

print_top_roles(pompey_magnus, projects)
print_top_roles(markus_crassus, projects)
print_top_roles(julius_caesar, projects)
print_top_roles(marc_antony, projects)
print_top_roles(marcus_cicero, projects)

consul.apply(pompey_magnus)
consul.apply(markus_crassus)
command.apply(julius_caesar)
command.apply(marc_antony)

select_and_print(consul, 2)
select_and_print(command, 1)

pompey_magnus.endorse(Endorsement("Skilled Administrator",
                                  Skill(Skills.Administration.name, 8)), marcus_cicero)
markus_crassus.endorse(Endorsement("Skilled Administrator",
                                   Skill(Skills.Administration.name, 8)), marcus_cicero)

julius_caesar.endorse(Endorsement(
    "Exceptional military commander", Skill(Skills.Martial.name, 10)), marc_antony)
julius_caesar.endorse(Endorsement(
    "Would follow anywhere.", Skill(Skills.Leadership.name, 10)), marcus_cicero)
julius_caesar.endorse(Endorsement(
    "Love this guy.", Skill(Skills.Charisma.name, 10)), marc_antony)

dictator = Role(Roles.Dictator.name, "Rule Rome.", RoleStatus.Open)
dictator.update_required_skill(Skill(Skills.Martial.name, 6))
dictator.update_required_skill(Skill(Skills.Leadership.name, 8))

dictator.update_bonus_skill(Skill(Skills.Charisma.name, 8))

dictator.apply(pompey_magnus)
dictator.apply(marc_antony)
dictator.apply(julius_caesar)

select_and_print(dictator, 1)
