from enum import Enum

class Abonnement(Enum):
    FORFAIT = "Forfait"
    TICKET = "Ticket"

    def __str__(self):
        return self.value