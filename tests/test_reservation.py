from datetime import datetime

from src.abonnement import Abonnement
from src.prix_avec_abonnement import PrixAvecAbonnement
from src.prix_sans_abonnement import PrixSansAbonnement
from src.reservation import Reservation
from src.temps_jeu import TempsJeu
from src.type_salle import TypeSalle
from src.salle import Salle
from src.adherent import Adherent
from pytest import raises

def test_calculer_prix_avec_forfait():
    reservation = Reservation(
        salle=Salle(id=1, type_salle=TypeSalle.TENNIS, capacite=1),
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
        salle=Salle(id=1, type_salle=TypeSalle.BADMINTON, capacite=1),
        type_salle=TypeSalle.BADMINTON,
        horaire=datetime(2024, 6, 1, 11, 0),
        abonnement=Abonnement.TICKET,
        temps_jeu=TempsJeu.BADMINTON,
        prix_sans_abonnement=PrixSansAbonnement.BADMINTON,
        prix_avec_abonnement=PrixAvecAbonnement.BADMINTON,
    )

    assert reservation.calculer_prix() == 20

def test_temps_jeu():
    reservation = Reservation(
        salle=Salle(id=1, type_salle=TypeSalle.SQUASH, capacite=1),
        type_salle=TypeSalle.SQUASH,
        horaire=datetime(2024, 6, 1, 12, 0),
        abonnement=Abonnement.TICKET,
        temps_jeu=TempsJeu.SQUASH,
        prix_sans_abonnement=PrixSansAbonnement.SQUASH,
        prix_avec_abonnement=PrixAvecAbonnement.SQUASH,
    )

    assert reservation.temps_jeu.value == 0.5


def test_reservation_salle_indisponible():
    salle = Salle(id=1, type_salle=TypeSalle.TENNIS, capacite=0, disponible=False)
    reservation = Reservation(
        salle=salle,
        type_salle=TypeSalle.TENNIS,
        horaire=datetime(2024, 6, 1, 10, 0),
        abonnement=Abonnement.FORFAIT,
        temps_jeu=TempsJeu.TENNIS,
        prix_sans_abonnement=PrixSansAbonnement.TENNIS,
        prix_avec_abonnement=PrixAvecAbonnement.TENNIS,
    )

    assert reservation.salle.est_disponible() is False

def test_reservation_salle_disponible():
    salle = Salle(id=1, type_salle=TypeSalle.BADMINTON, capacite=2)
    adherent = Adherent(id=1, type_abonnement=Abonnement.TICKET, solde=100)
    reservation = Reservation(
        salle=salle,
        type_salle=TypeSalle.BADMINTON,
        horaire=datetime(2024, 6, 1, 11, 0),
        abonnement=Abonnement.TICKET,
        temps_jeu=TempsJeu.BADMINTON,
        prix_sans_abonnement=PrixSansAbonnement.BADMINTON,
        prix_avec_abonnement=PrixAvecAbonnement.BADMINTON,
    )

    assert reservation.salle.est_disponible() is True

    salle.reserver(adherent)
    assert reservation.salle.capacite == 1

def test_reservation_si_solde_insuffisant():
    salle = Salle(id=1, type_salle=TypeSalle.SQUASH, capacite=1)
    adherent = Adherent(id=1, type_abonnement=Abonnement.TICKET, solde=10)
    reservation = Reservation(
        salle=salle,
        type_salle=TypeSalle.SQUASH,
        horaire=datetime(2024, 6, 1, 12, 0),
        abonnement=Abonnement.TICKET,
        temps_jeu=TempsJeu.SQUASH,
        prix_sans_abonnement=PrixSansAbonnement.SQUASH,
        prix_avec_abonnement=PrixAvecAbonnement.SQUASH,
    )

    assert reservation.calculer_prix() == 15
    assert adherent.solde < reservation.calculer_prix() 
    with raises(ValueError):
        adherent.payer(reservation.calculer_prix())
    

