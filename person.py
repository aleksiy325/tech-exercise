from typing import Dict, List
from skill import Skill
from endorsement import Endorsement


class Person():
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.skills: Dict[str, Skill] = {}
        self.endorsements: List[Endorsement] = []
