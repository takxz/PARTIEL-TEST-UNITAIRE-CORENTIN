from enum import Enum

class TypeSalle(Enum):
    TENNIS = "Salle de Tennis"
    BADMINTON = "Salle de Badminton"
    SQUASH = "Salle de Squash"

    def __str__(self):
        return self.value