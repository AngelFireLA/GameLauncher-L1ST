from ..utils import récupérer_combinaison_aléatoire

class Partie:
    def __init__(self):
        self.combinaison = récupérer_combinaison_aléatoire()
        self.progrès = [-1, -1, -1, -1]

    def tester_combinaison(self, combinaison):
        if combinaison == self.combinaison:
            return True
        else:
            self.progrès = [-1, -1, -1, -1]
            for i in range(4):
                if combinaison[i] == self.combinaison[i]:
                    self.progrès[i] = 2
                elif combinaison[i] not in self.combinaison:
                    self.progrès[i] = 0
            mauvaise_position = {"rouge":0, "vert":0, "bleu":0, "jaune":0, "orange":0, "rose":0}
            for i in range(4):
                if self.progrès[i] == -1:
                    print(i, combinaison[i], mauvaise_position, self.combinaison.count(combinaison[i]))
                    if self.combinaison.count(combinaison[i]) > mauvaise_position[combinaison[i]]:
                        self.progrès[i] = 1
                        mauvaise_position[combinaison[i]] += 1

            return False
