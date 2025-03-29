import random
class Partie:
    def __init__(self, taille=10, mode="normal"):
        self.taille = taille
        self.tours = self.initialiser_tours(mode)
        self.coups = 0

    def initialiser_tours(self, mode):
        tours = [[] for _ in range(3)]
        if mode == "normal":
            tours[0] = list(range(self.taille, 0, -1))
        elif mode == "aléatoire":
            for anneaux_restants in range(self.taille, 0, -1):
                tour_random = random.randint(0, 2)
                tours[tour_random].append(anneaux_restants)
        return tours

    def bouger(self, tour1, tour2):
        if tour1 == tour2:
            return
        if tour1:
            if not tour2 or tour1[-1] < tour2[-1]:
                tour2.append(tour1.pop())
                self.coups += 1

# partie = Partie()
# while True:
#     print(partie.tours)
#     tour1 = int(input("Tour de départ: "))
#     tour2 = int(input("Tour d'arrivée: "))
#     partie.bouger(tour1, tour2)