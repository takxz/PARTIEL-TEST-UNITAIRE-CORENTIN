from datetime import datetime

from src.abonnement import Abonnement
from src.prix_avec_abonnement import PrixAvecAbonnement
from src.prix_sans_abonnement import PrixSansAbonnement
from src.reservation import Reservation
from src.temps_jeu import TempsJeu
from src.type_salle import TypeSalle

def test_calculer_prix_avec_forfait():
    reservation = Reservation(
        type_salle=TypeSalle.TENNIS,
        horaire=datetime(2024, 6, 1, 10, 0),
        abonnement=Abonnement.FORFAIT,
        temps_jeu=TempsJeu.TENNIS,
        prix_sans_abonnement=PrixSansAbonnement.TENNIS,
        prix_avec_abonnement=PrixAvecAbonnement.TENNIS,
    )

    assert reservation.calculer_prix() == 11


def test_calculer_prix_avec_ticket():
    reservation = Reservation(
        type_salle=TypeSalle.BADMINTON,
        horaire=datetime(2024, 6, 1, 11, 0),
        abonnement=Abonnement.TICKET,
        temps_jeu=TempsJeu.BADMINTON,
        prix_sans_abonnement=PrixSansAbonnement.BADMINTON,
        prix_avec_abonnement=PrixAvecAbonnement.BADMINTON,
    )

    assert reservation.calculer_prix() == 20