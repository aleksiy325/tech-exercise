from skill import Skill


class Endorsement():
    def __init__(self, feedback: str, skill: Skill) -> None:
        self.feedback: str = feedback
        self.skill: Skill = skill

    def __str__(self):
        return '{} {}: {}'.format(self.skill.experience_rating, self.skill.name, self.feedback)
