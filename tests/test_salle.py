import pytest

from src.abonnement import Abonnement
from src.adherent import Adherent
from src.salle import Salle
from src.type_salle import TypeSalle

def test_est_disponible():
    salle = Salle(id=1, type_salle=TypeSalle.TENNIS, capacite=2)
    assert salle.est_disponible() is True

def test_reserver():
    salle = Salle(id=1, type_salle=TypeSalle.TENNIS, capacite=1)
    adherent = Adherent(id=1, type_abonnement=Abonnement.TICKET, solde=100)
    salle.reserver(adherent)
    assert salle.inscrit == [adherent]
    assert salle.capacite == 0
    assert salle.disponible is False


def test_reserver_deux_fois_avec_capacite_deux():
    salle = Salle(id=1, type_salle=TypeSalle.BADMINTON, capacite=2)
    adherent_1 = Adherent(id=1, type_abonnement=Abonnement.TICKET, solde=100)
    adherent_2 = Adherent(id=2, type_abonnement=Abonnement.FORFAIT, solde=100)

    salle.reserver(adherent_1)
    assert salle.est_disponible() is True
    assert salle.capacite == 1

    salle.reserver(adherent_2)
    assert salle.est_disponible() is False
    assert salle.capacite == 0
    assert salle.inscrit == [adherent_1, adherent_2]


def test_reserver_salle_non_disponible_leve_une_erreur():
    salle = Salle(id=1, type_salle=TypeSalle.SQUASH, capacite=0, disponible=False)
    adherent = Adherent(id=1, type_abonnement=Abonnement.TICKET, solde=100)

    with pytest.raises(ValueError):
        salle.reserver(adherent)