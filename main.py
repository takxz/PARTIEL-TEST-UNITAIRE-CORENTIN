from src.adherent import Adherent
from src.abonnement import Abonnement
from src.salle import Salle
from src.type_salle import TypeSalle
from src.reservation import Reservation
from src.temps_jeu import TempsJeu
from src.prix_sans_abonnement import PrixSansAbonnement
from src.prix_avec_abonnement import PrixAvecAbonnement
from datetime import datetime


def main():
    salle1 = Salle(id=1, type_salle=TypeSalle.TENNIS, capacite=1)
    salle2 = Salle(id=2, type_salle=TypeSalle.BADMINTON, capacite=1)
    adherent1 = Adherent(id=1, type_abonnement=Abonnement.FORFAIT, solde=100)
    adherent2 = Adherent(id=2, type_abonnement=Abonnement.TICKET, solde=50)
    reservation = Reservation(
        salle=salle1,
        type_salle=TypeSalle.TENNIS,
        horaire=datetime(2024, 6, 1, 10, 0),
        abonnement=Abonnement.FORFAIT,
        temps_jeu=TempsJeu.TENNIS,
        prix_sans_abonnement=PrixSansAbonnement.TENNIS,
        prix_avec_abonnement=PrixAvecAbonnement.TENNIS,
    )
    print(adherent1)
    print(adherent2)
    print(salle1)
    print(salle2)
    print(f"Prix de la réservation : {reservation.calculer_prix()}")

    salle1.reserver(adherent1)
    print(salle1)


   #salle1.reserver(adherent2)  #Erreur

if __name__ == "__main__":
    main()