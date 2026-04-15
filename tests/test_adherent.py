from src.adherent import Adherent
from src.abonnement import Abonnement

def test_representation_adherent():

    adherent = Adherent(id=1, type_abonnement=Abonnement.FORFAIT, solde=100)
    assert repr(adherent) == "Adherent(id=1, type_abonnement=Abonnement.FORFAIT, solde=100)"