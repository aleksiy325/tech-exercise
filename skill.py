class Skill():
    def __init__(self, name: str, experience_rating: int) -> None:
        self.name: str = name
        self.experience_rating: int = experience_rating

    def meets(self, other):
        return self.name == other.name and self.experience_rating >= other.experience_rating

    def __str__(self):
        s = self.name + ' ' + str(self.experience_rating)
        return s
