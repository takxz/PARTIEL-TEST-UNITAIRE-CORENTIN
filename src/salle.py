from src.type_salle import TypeSalle
from src.adherent import Adherent

class Salle:
    def __init__(self, id: int, type_salle: TypeSalle, capacite: int, inscrit: list[Adherent] | None = None, disponible: bool = True):
        self.id = id
        self.type_salle = type_salle
        self.capacite = capacite
        self.inscrit = inscrit or []
        self.disponible = disponible and capacite > 0

    def __repr__(self):
        return f"Salle(id={self.id}, type_salle={self.type_salle}, capacite={self.capacite}, inscrit={self.inscrit}, disponible={self.disponible})"
    

    def est_disponible(self):
        return self.disponible and self.capacite > 0
    
    def reserver(self, adherent: Adherent):
        if not self.est_disponible():
            raise ValueError("Salle indisponible ou capacité insuffisante.")

        self.inscrit.append(adherent)
        self.capacite -= 1

        if self.capacite == 0:
            self.disponible = False

    
