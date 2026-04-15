from src.adherent import Adherent
from src.abonnement import Abonnement
from src.salle import Salle
from src.type_salle import TypeSalle


def main():
    salle1 = Salle(id=1, type_salle=TypeSalle.TENNIS, capacite=1)
    salle2 = Salle(id=2, type_salle=TypeSalle.BADMINTON, capacite=1)
    adherent1 = Adherent(id=1, type_abonnement=Abonnement.FORFAIT, solde=100)
    adherent2 = Adherent(id=2, type_abonnement=Abonnement.TICKET, solde=50)
    print(adherent1)
    print(adherent2)
    print(salle1)
    print(salle2)

    salle1.reserver(adherent1)
    print(salle1)
   #salle1.reserver(adherent2)  #Erreur

if __name__ == "__main__":
    main()