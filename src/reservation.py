from src.temps_jeu import TempsJeu
from src.prix_avec_abonnement import PrixAvecAbonnement
from src.prix_sans_abonnement import PrixSansAbonnement
from src.abonnement import Abonnement
from src.type_salle import TypeSalle
from datetime import datetime
from src.salle import Salle

class Reservation:
    def __init__(self, salle: Salle, type_salle: TypeSalle, horaire: datetime, abonnement: Abonnement, temps_jeu: TempsJeu, prix_sans_abonnement: PrixSansAbonnement, prix_avec_abonnement: PrixAvecAbonnement):
        self.salle = salle
        self.type_salle = type_salle
        self.horaire = horaire
        self.abonnement = abonnement
        self.temps_jeu = temps_jeu
        self.prix_sans_abonnement = prix_sans_abonnement
        self.prix_avec_abonnement = prix_avec_abonnement

    def calculer_prix(self):
        if self.abonnement == Abonnement.FORFAIT:
            return self.prix_avec_abonnement.value
        else:
            return self.prix_sans_abonnement.value
    