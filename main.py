from src.adherent import Adherent
from src.abonnement import Abonnement

def main():
    adherent1 = Adherent(id=1, type_abonnement=Abonnement.FORFAIT, solde=100)
    adherent2 = Adherent(id=2, type_abonnement=Abonnement.TICKET, solde=50)
    print(adherent1)
    print(adherent2)

if __name__ == "__main__":
    main()