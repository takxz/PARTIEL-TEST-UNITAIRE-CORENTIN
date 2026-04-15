from src.adherent import Adherent
from src.abonnement import Abonnement
from pytest import raises

def test_representation_adherent():

    adherent = Adherent(id=1, type_abonnement=Abonnement.FORFAIT, solde=100)
    assert repr(adherent) == "Adherent(id=1, type_abonnement=Forfait, solde=100)"

def test_peut_payer():
    adherent = Adherent(id=1, type_abonnement=Abonnement.TICKET, solde=50)
    assert adherent.peut_payer(30) is True
    assert adherent.peut_payer(50) is True
    assert adherent.peut_payer(51) is False

def test_payer():
    adherent = Adherent(id=1, type_abonnement=Abonnement.FORFAIT, solde=100)
    adherent.payer(30)
    assert adherent.solde == 70

    adherent.payer(50)
    assert adherent.solde == 20

    with raises(ValueError):
        adherent.payer(25)