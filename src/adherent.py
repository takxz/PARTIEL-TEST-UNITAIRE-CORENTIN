from src.abonnement import Abonnement

class Adherent:
    def __init__(self, id: int, type_abonnement: Abonnement, solde: int = 0):
        self.id = id
        self.type_abonnement = type_abonnement
        self.solde = solde

    
    def __repr__(self):
        return f"Adherent(id={self.id}, type_abonnement={self.type_abonnement}, solde={self.solde})"

    