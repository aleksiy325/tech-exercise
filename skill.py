class Skill():
    def __init__(self, name: str, experience_level: int) -> None:
        self.name: str = name
        self.experience_level: int = experience_level

    def meets(self, other):
        return self.name == other.name and self.experience_level >= other.experience_level
